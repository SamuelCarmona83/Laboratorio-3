import os
import psycopg2

PATH = os.path.dirname(os.path.abspath(__file__))
FILES = os.listdir(PATH)

conn = psycopg2.connect(database="postgres", user="admin", password="123456", host="localhost", port="5432")

conn.set_isolation_level(psycopg2.extensions.ISOLATION_LEVEL_AUTOCOMMIT)
cur = conn.cursor()

print "\nInicio de restauración de Bases de Datos\n\n"

for F in FILES:
  
    if F[F.__len__()-4:] == ".tar" and F.rfind("postgres.tar") < 0 and F.rfind("template") < 0:
        print "\nRestaurando la Base de Datos: %s\n" % F[:-14]
        try:
            cur.execute('CREATE DATABASE "%s"' % F[:-14])
            os.system("psql -U postgres -d %s -1 -f %s" % (F[:-14], F))
            print "\nLa Base de Datos %s restaurada con exito\n" % F[:-4]
        except Exception, e:
            print "\nError al reataurar la Base de Datos %s.\nDetalles: %s\n" % (F[:-4], e)