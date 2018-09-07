import os
from socket import *
from oscphys import getDragForce, getMaxSpeed
import math
#host = "172.0.0.1"
#host = "192.168.205.51" # set to IP address of target computer
host = "localhost"
#host = "192.168.205.1"
port = 5675
addr = (host, port)
UDPSock = socket(AF_INET, SOCK_DGRAM)


def simpleDecoder(data):
	return data.split("  ")

frontalArea = 2
airDensity = 1.225
dragCoefficient = 0.1
force = 2
mass = 1


def encodeAndSend(data):
	data = data.encode('utf-8')
	UDPSock.sendto(data, addr)
	
def setUPDragChart():
	encodeAndSend("setValueDesc  Acc. Dc = " + str(dragCoefficient))
	encodeAndSend("setNDesc  Speed (v) in second")
	mxs = getMaxSpeed(force, frontalArea, airDensity, dragCoefficient)
	mx = int(math.ceil(mxs))
	encodeAndSend("setNScale  " + str(mx / 10))
	for i in range(mx):
		n = i + 1
		df = getDragForce(n, frontalArea, airDensity, dragCoefficient)
		acc = (force - df) / mass
		encodeAndSend("addBlock  {0}  {1}".format(str(n), str(acc)))
	
setUPDragChart()

while True:
	#data = raw_input("Enter message to send or type 'exit': ")
	data = input("Enter message to send or type 'exit': ")
	if data == "exit":
		data = data.encode('utf-8')
		UDPSock.sendto(data, addr)
		break
	elif data == "port":
		data = input("Masukan portnya: ")
		addr = (host, int(data))
	elif data == "frontalArea":
		value = input("frontalArea = ")
		frontalArea = float(value)
	elif data == "airDensity":
		value = input("airDensity = ")
		airDensity = float(value)
	elif data == "dragCoefficient":
		value = input("dragCoefficient = ")
		dragCoefficient = float(value)
	elif data == "force":
		value = input("force = ")
		force = float(value)
	elif data == "mass":
		value = input("mass = ")
		mass = float(value)
	elif data == "start":
		setUPDragChart()
	elif data == "restart":
		data = data.encode('utf-8')
		UDPSock.sendto(data, addr)
	else:
		data = data.encode('utf-8')
		UDPSock.sendto(data, addr)
UDPSock.close()
os._exit(0)