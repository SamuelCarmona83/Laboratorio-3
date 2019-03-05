#!/usr/bin/python
#sudo service postgresql start
import sys
import psycopg2
import os
import datetime


myConnection = psycopg2.connect(host = 'localhost', user= 'postgres', password ='postgres', dbname= 'cerveza', port="5432")

# Nombre de la base de datos que deseas respaldar
database = 'store'

def doBackup():
    cur = myConnection.cursor()

    #en realidad hice esto para ver si coincide o hacer respaldos en rangos de un cluster
    cur.execute("SELECT datname FROM pg_database WHERE datname='%s'" % database)
    rows = cur.fetchall()
    #print(rows)

    print ("Inicio del proceso de Respaldo de las Bases de Datos:\n")

    for row in rows:
    	try:
            print ("Respaldando Base de Datos: %s\n" % database)
            os.system("pg_dump -U postgres %s > %s.tar" % (database, database+str( datetime.date.today() ) ))
        	
            print ("Base de Datos %s respaldada con éxito\n" % database )
    	except Exception as e:
        	print ("Error al respaldar la Base de Datos %s.\nDetalles: %s\n" % (database, e))

def main():	
	doBackup()

if __name__ == '__main__':
	main()
	sys.exit(0)
