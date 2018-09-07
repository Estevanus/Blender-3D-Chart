import bge
import gameObjects


def setupXNumber(cont):
	own = gameObjects.KX_xNomber(cont.owner)
	for i in cont.actuators:
		cont.activate(i)
	
def setupYNumber(cont):
	own = gameObjects.KX_yNomber(cont.owner)
	for i in cont.actuators:
		cont.activate(i)
	
def runClass(cont):
	cont.owner.run()
	
'''
def addX(cont):
	own = cont.owner
	if hasattr(own, "i"):
		if own.i <= 10:
			own.position.x = i
			own.i += 1
	else
		own.i = 0
	
def addY(cont):
	own = cont.owner
	if hasattr(own, "i"):
		if own.i <= 10:
			own.position.z = i
			own.i += 1
	else
		own.i = 0
'''

def addX(cont):
	own = cont.owner
	for i in range(10):
		own.position.x = i + 1
		own.scene.addObject("x", own)

def addY(cont):
	own = cont.owner
	for i in range(10):
		own.position.z = i + 1
		own.scene.addObject("y", own)
		

def setupBlockAdder(cont):
	own = gameObjects.KX_BlockAdder(cont.owner)
	for i in cont.actuators:
		cont.activate(i)
		
def setupCam(cont):
	own = gameObjects.KX_CamPos(cont.owner)
	for i in cont.actuators:
		cont.activate(i)

def runBlockAdder(cont):
	cont.owner.run();
	
def close(cont):
	cont.owner.close()