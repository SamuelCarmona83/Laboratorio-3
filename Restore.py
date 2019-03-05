import os
import psycopg2

PATH = os.path.dirname(os.path.abspath(__file__))
FILES = os.listdir(PATH) # Recupera los nombres de los archivos en el directorio especificado

conn = psycopg2.connect(user="postgres", password="postgres", host="localhost", port="5432")

conn.set_isolation_level(psycopg2.extensions.ISOLATION_LEVEL_AUTOCOMMIT)
cur = conn.cursor()

print ("\nInicio de restauración de Bases de Datos\n\n")

# Recorre y recupera las bases de datos en el directorio
for F in FILES:
    if F[F.__len__()-4:] == ".tar" and F.rfind("postgres.tar") < 0 and F.rfind("template") < 0:
        print ("\nRestaurando la Base de Datos: %s\n" % F[:-14])
        try:
            cur.execute('CREATE DATABASE "%s";' % F[:-14])
            os.system("psql -U postgres -d %s -1 -f %s" % (F[:-14], F))
            # No es posible recuperar mediante pg_restore por conflicostos con los formatos
            # de Manera parcial elegi el formato Tar, puede ser .bak o hasta .sql
            # Si arreglo esa problamatica es imposible realizar el restore para bases de datos muy grandes
            # De igual manera el comando es de la forma
            # "pg_restore -h <Host> -U <User> -O -x -d %s %s" % (F[:-14], F) 
            print ("\nLa Base de Datos %s restaurada con exito\n" % F[:-14])
        
        except Exception as e:
            print ("\nError al restaurar la Base de Datos %s.\nDetalles: %s\n" % (F[:-4], e))