from __future__ import division
from pypxlib import Table
import csv
import math
import sys, getopt

def main(argv):

  try:
    opts, args = getopt.getopt(argv,"hi:o:c:x",["ifile=","ofile=","headers=","headershelp="])
  except getopt.GetoptError:
    print 'paradoxdbsplitter.py -i <inputfile> -o <outputfile>'
    sys.exit(2)
  for opt, arg in opts:
    if opt == '-h':
       print 'paradoxdbsplitter.py -i <inputfile> -o <outputfile> -c <headers(hola,adios,pepe)>'
       sys.exit()
    elif opt in ("-x", "--helpheaders"):
      headershelp = 1
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

  if 'headershelp' in locals():
    print(table[0])
    sys.exit()

  registros = len(table)
  print "Dimension filas tabla: %s." % registros
  print "Cantidad de registros por fichero: %d." % bloque
  print "Cabeceras que se van a usar: %s." % cabeceras
  print "Ruta del archivo: %s." % inputfile

  print registros
  print bloque
  print registros/bloque
  print math.ceil(registros/bloque)

  iteraciones = int(math.ceil(registros/bloque))

  print "Ficheros que se van a generar: %s." % iteraciones

  iteracion = 0

  for iteracion in range(0, iteraciones):

    print "iteracion numero %s" % iteracion
    with open(outputfile+"_parte_"+str(iteracion)+".csv", "wb") as csvfile:

        spamwriter = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        # headers
        spamwriter.writerow(cabeceras)
	start = iteracion * bloque
	end = start + bloque
        if end > registros:
          end = registros

        for row in range(start, end):

          #print start
          spamwriter.writerow([table[row][s].encode('utf8') if type(table[row][s]) is unicode else table[row][s] for s in cabeceras])

if __name__ == "__main__":
   main(sys.argv[1:])
