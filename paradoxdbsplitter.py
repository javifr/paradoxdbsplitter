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
       fileheaders = arg.split(",")


  file_rows_size = 100000
  table = Table(inputfile)

  if 'headershelp' in locals():
    print(table[0])
    sys.exit()

  table_rows_count = len(table)
  iterations = table_rows_count/file_rows_size

  print "Table rows: %s." % table_rows_count
  print "Rows per file: %d." % file_rows_size
  print "File headers to be extracted: %s." % fileheaders
  print "File (db) path: %s." % inputfile
  print "File parts about to generate: %s." % iterations

  iteration = 0

  for iteration in range(0, iterations-1):

    with open(outputfile+"_parte_"+str(iteration)+".csv", "wb") as csvfile:

        # file ready
        spamwriter = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        # write headers
        spamwriter.writerow(fileheaders)

        # write db lines to csv
        for row in range(iteration*file_rows_size, (iteration*file_rows_size)+file_rows_size):
          spamwriter.writerow([table[row].NumeroSocio,table[row].FechaAsistencia,table[row].HoraAsistencia,table[row].PuestoEntrada,table[row].AnyoAsistencia,table[row].MesAsistencia,table[row].DiaAsistencia,table[row].Hora])

if __name__ == "__main__":
   main(sys.argv[1:])