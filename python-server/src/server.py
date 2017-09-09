import socket
import json
from pymongo import MongoClient
# pprint library is used to make the output look more pretty
from pprint import pprint

def mongoinsert(jdata):
    # connect to MongoDB
    client = MongoClient("mongodb://brewlog_db_1")
    db=client.testbrew
    db.testbrew.insert_one(jdata)
    # Issue the serverStatus command and print the results
    #serverStatusResult=db.command("serverStatus")
    #pprint(serverStatusResult)

if __name__ == '__main__':
   s = socket.socket()         # Create a socket object
   host = socket.gethostname() # Get local machine name
   port = 12346                # Reserve a port for your service.
   s.bind((host, port))        # Bind to the port

   s.listen(5)                 # Now wait for client connection.
   while True:
      c, addr = s.accept()     # Establish connection with client.
      print 'Got connection from', addr
      data = c.recv(1024)
      jdata = json.loads(data.decode('utf-8'))
      colour = jdata['Colour']
      name = jdata['Beer']
      tempf = jdata['Temp']
      temp = (tempf -32) * 5.0/9.0
      time = jdata['Time']
      sg = jdata['SG']
      mongoinsert(jdata)
# print received data to stdout
      print jdata['Colour']
      print jdata['Beer']
      print jdata['Temp']
      print jdata['SG']
      print jdata['Time']
      c.send('Data Received')
      c.close()
