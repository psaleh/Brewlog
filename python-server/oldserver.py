#!/usr/bin/python           # This is server.py file

import socket               # Import socket module
import json                 # Import JSON Module
import mysql.connector
from mysql.connector import Error
#import csv

def connect(name, colour, sg, temp):
    query = "INSERT INTO testtable (Name,Colour,SG,temp) VALUES(%s,%s,%s,%s)"
    args = (name, colour, sg, temp)


    """ Connect to MySQL database """
    try:
        conn = mysql.connector.connect(host='brewlog_db_1',
                                       database='brewlog',
                                       user='brewlog',
                                       password='brewlog')
        if conn.is_connected():
            print('Connected to MySQL database')

            cursor = conn.cursor()
            cursor.execute(query, args)

            if cursor.lastrowid:
               print('last insert id', cursor.lastrowid)
            else:
               print('last insert id not found')

            conn.commit()

    except Error as e:
        print(e)

    finally:
        conn.close()
        conn.close()



if __name__ == '__main__':
   s = socket.socket()         # Create a socket object
   host = socket.gethostname() # Get local machine name
   port = 12345                # Reserve a port for your service.
   s.bind((host, port))        # Bind to the port

   s.listen(5)                 # Now wait for client connection.
   while True:
      c, addr = s.accept()     # Establish connection with client.
      print 'Got connection from', addr
      data = c.recv(1024)
      jdata = json.loads(data.decode('utf-8'))
      colour = jdata['Colour']
      name = jdata['Beer']
      temp = jdata['Temp']
      temp = (temp - 32)*0.5556
      time = jdata['Time']
      sg = jdata['SG']
      connect(name, colour, sg, temp)
# print received data to stdout
      print jdata['Colour']
      print jdata['Beer']
      print jdata['Temp']
      print jdata['SG']
      print jdata['Time']
      c.send('Data Received')
      c.close()                # Close the connection
                         
