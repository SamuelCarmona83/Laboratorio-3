#!/usr/bin/python
import ssl
import sys
import psycopg2
import json
import os

myConnection = psycopg2.connect(host = 'localhost', user= 'postgres', password ='postgres', dbname= 'store', port="5432")


def Query():
    cur = myConnection.cursor()
    #cur.execute("INSERT")
    rows = 200

    for i in range(100,rows+1):
    	try:
    		#cur.execute("INSERT INTO user_1 (user_id,balance_amount,name,shopcar_id) VALUES (%i,%f,%s,%s);" % (i,i+1.2,'2','15') )
    		#cur.execute("INSERT INTO shopping_car (shopcar_id,user_id,products_id,number) VALUES (%s,%i,%i,%i);" % (str(i),i,i,15) )
    		cur.execute("INSERT INTO product_table (product_id,shopcar_id,aviable_amount,price_peer_unit) VALUES (%i,%s,%i,%f);" % (i+2,str(i),2+i,i-1.7))
    		myConnection.commit()
    	except Exception as e:
        	print ("Error.\nDetalles: %s\n" %  e )

def main():	
	Query()

if __name__ == '__main__':
	main()
	sys.exit(0)