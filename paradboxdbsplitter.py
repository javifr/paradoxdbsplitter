from pypxlib import Table
import csv
import math
import sys, getopt

def main(argv):

  try:
    opts, args = getopt.getopt(argv,"hi:o:c",["ifile=","ofile=","headers="])
  except getopt.GetoptError:
    print 'paradoxdbsplitter.py -i <inputfile> -o <outputfile>'
    sys.exit(2)
  for opt, arg in opts:
    if opt == '-h':
       print 'paradoxdbsplitter.py -i <inputfile> -o <outputfile> -c <headers(hola,adios,pepe)>'
       sys.exit()
    elif opt in ("-i", "--ifile"):
       inputfile = arg
    elif opt in ("-o", "--ofile"):
       outputfile = arg
    elif opt in ("-c", "--headers"):
       cabeceras = arg.split(",")
    # elif opt in ("-b", "--block"):
    #    bloque = arg

  bloque = 100000
  table = Table(inputfile)

  registros = len(table)
  print "Dimension filas tabla: %s." % registros
  print "Cantidad de registros por fichero: %d." % bloque
  print "Cabeceras que se van a usar: %s." % cabeceras
  print "Ruta del archivo: %s." % inputfile

  iteraciones = registros/bloque

  print "Ficheros que se van a generar: %s." % iteraciones

  iteracion = 0

  for iteracion in range(0, iteraciones-1):

    with open(outputfile+"_parte_"+str(iteracion)+".csv", "wb") as csvfile:

        spamwriter = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        # headers
        spamwriter.writerow(cabeceras)

        for row in range(0, iteracion+bloque):
          spamwriter.writerow([table[row].NumeroSocio,table[row].FechaAsistencia,table[row].HoraAsistencia,table[row].PuestoEntrada,table[row].AnyoAsistencia,table[row].MesAsistencia,table[row].DiaAsistencia,table[row].Hora])

if __name__ == "__main__":
   main(sys.argv[1:])