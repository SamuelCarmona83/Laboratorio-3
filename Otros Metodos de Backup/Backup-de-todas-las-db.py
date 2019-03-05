#!/usr/bin/python
#sudo service postgresql start

import ssl
import sys
import psycopg2
import json
import os

myConnection = psycopg2.connect(host = 'localhost', user= 'postgres', password ='postgres', dbname= 'cerveza', port="5432")


def doBackup():
    cur = myConnection.cursor()
    cur.execute("SELECT datname FROM pg_database")
    rows = cur.fetchall()
    
    #print(rows)
    
    print ("Inicio del proceso de Respaldo de las Bases de Datos:\n")

    for row in rows:
    	try:
        	print ("Respaldando Base de Datos: %s\n" % row[0])
        	os.system("pg_dump -U postgres %s > %s.tar" % (row[0], row[0]))
            # tambien es posible hacerlo com pg_dumpall pero este metodo es más flexible
        	print ("Base de Datos %s respaldada con éxito\n" % row[0])
    	except Exception as e:
        	print ("Error al respaldar la Base de Datos %s.\nDetalles: %s\n" % (row[0], e))

def main():	
	doBackup()

if __name__ == '__main__':
	main()
	sys.exit(0)
