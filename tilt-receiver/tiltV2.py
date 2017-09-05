import blescan
import sys
import requests
import datetime
import time
import bluetooth._bluetooth as bluez
import pygame
import os
import socket
import json

#Assign uuid's of various colour tilt hydrometers. BLE devices like the tilt work primarily using advertisements. 
#The first section of any advertisement is the universally unique identifier. Tilt uses a particular identifier based on the colour of the device
red    	= 'a495bb10c5b14b44b5121370f02d74de'
green  	= 'a495bb20c5b14b44b5121370f02d74de'
black  	= 'a495bb30c5b14b44b5121370f02d74de'
purple 	= 'a495bb40c5b14b44b5121370f02d74de'
orange 	= 'a495bb50c5b14b44b5121370f02d74de'
blue   	= 'a495bb60c5b14b44b5121370f02d74de'
yellow 	= 'a495bb70c5b14b44b5121370f02d74de'
pink   	= 'a495bb80c5b14b44b5121370f02d74de'

#The default device for bluetooth scan. If you're using a bluetooth dongle you may have to change this.
dev_id = 0

#function to calculate the number of days since epoch (used by google sheets)
#In python time.time() gives number of seconds since epoch (Jan 1 1970).
#Google Sheets datetime as a number is the number of days since the epoch except their epoch date is Jan 1 1900
def sheetsDate(date1):
	temp = datetime.datetime(1899, 12, 30)
	delta=date1-temp
	return float(delta.days) + (float(delta.seconds) / 86400)

#scan BLE advertisements until we see one matching our tilt uuid
def getdata():
	try:
		sock = bluez.hci_open_dev(dev_id)

	except:
		print "error accessing bluetooth device..."
		sys.exit(1)

	blescan.hci_le_set_scan_parameters(sock)
	blescan.hci_enable_le_scan(sock)

	gotData = 0
	while (gotData == 0):

		returnedList = blescan.parse_events(sock, 10)

		for beacon in returnedList: #returnedList is a list datatype of string datatypes seperated by commas (,)
			output = beacon.split(',') #split the list into individual strings in an array
			if output[1] == green: #Change this to the colour of you tilt
				tempf = float(output[2]) #convert the string for the temperature to a float type

				gotData = 1

				tiltTime = sheetsDate(datetime.datetime.now())
				tiltSG = float(output[3])/1000
				tiltTemp = tempf
				tiltColour = 'GREEN'
				tiltBeer = 'TestBrew' #Change to an identifier of a particular brew

	#assign values to a dictionary variable for the http POST to google sheet
        data = dict()
        data['Time'] = tiltTime
        data['Colour'] = tiltColour
        data['Beer'] = tiltBeer
        data['Temp'] = tiltTemp
        data['SG'] = tiltSG
        jsonObj = json.dumps(data)
        #print jsonObj

	blescan.hci_disable_le_scan(sock)
	return jsonObj
		

def main():

	global screen

	updateSecs = 10 #time in seconds between updating the google sheet
	
	timestamp = time.time() #Set time for beginning of loop
	updateTime = timestamp + updateSecs #Set the time for the next update to google sheets

	while True:
		jsonObj = getdata()
		
		if time.time() > updateTime: #if we've reached the update time send data over socket and reset the updateTime
                        s = socket.socket()         # Create a socket object
                        host = "13.228.148.72"  # Get local machine name
                        port = 12345                # Reserve a port for your service.
			s.connect((host, port))
			s.sendall(jsonObj)
			print s.recv(1024)
			s.close                     # Close the socket when done
 
			updateTime = updateTime + updateSecs
			


if __name__ == "__main__": #dont run this as a module
	main()
