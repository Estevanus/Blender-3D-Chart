import bge
import var
import checker
from socket import AF_INET, SOCK_DGRAM
from socket import socket as sock
import math
from mathutils import *

def simpleDecoder(data):
	return data.split("  ")
	
class KX_xNomber(bge.types.KX_FontObject):
	def __init__(self, old_owner):
		pass
		
	def refresh(self):
		ke = round(self.position.x * var.xScale, 1)
		self.children[0].text = str(ke)
		self.scaling = [var.valueTextScale, var.valueTextScale, var.valueTextScale]
		#self.position.x -= 0.5
	
class KX_yNomber(bge.types.KX_FontObject):
	def __init__(self, old_owner):
		pass
		
	def refresh(self):
		ke = round(self.position.z / var.yScale, 1)
		self.children[0].text = str(ke)
		self.scaling = [var.valueTextScale, var.valueTextScale, var.valueTextScale]
		
class KX_x_adder(bge.types.KX_GameObject):
	def __init__(self, old_owner):
		self.nl = []
		for i in range(10):
			self.position.x = i + 1
			added = KX_xNomber(self.scene.addObject("x", self))
			self.nl.append(added)
			
	def refresh(self):
		for n in self.nl:
			n.refresh()
		
class KX_y_adder(bge.types.KX_GameObject):
	def __init__(self, old_owner):
		self.nl = []
		for i in range(10):
			self.position.z = i + 1
			added = KX_yNomber(self.scene.addObject("y", self))
			self.nl.append(added)
			
	def refresh(self):
		for n in self.nl:
			n.refresh()

class KX_Block(bge.types.KX_GameObject):
	def __init__(self, old_owner):
		self.nilai = 1
		self.n = 1
		pass
		
	def refresh(self):
		self.position.x = self.n / var.xScale
		self.scaling = [var.xScale / var.xScale**2, 1, var.yScale * self.nilai]
		
	def run(self):
		pass

class KX_BlockAdder(bge.types.KX_GameObject):
	def __init__(self, old_owner):
		self.shock = sock(AF_INET, SOCK_DGRAM)
		self.shock.bind(("", var.port))
		#self.shock.settimeout(0.01)
		self.shock.settimeout(0.01)
		
		self.blocks = []
		
		self.x_adder = KX_x_adder(self.scene.objects['x_adder'])
		self.y_adder = KX_y_adder(self.scene.objects['y_adder'])
		
		self.x_adder.refresh()
		self.y_adder.refresh()
		
		self.nDeskripsi = self.scene.objects["n info"]
		self.valueDeskripsi = self.scene.objects["ValueInfo"]
		
		self.cam = KX_CamPos(self.scene.objects['Camera'])
		
	def addBlock(self, value, n):
		self.position.x = n / var.xScale
		added = KX_Block(self.scene.addObject("block", self))
		self.blocks.append(added)
		added.nilai = value
		added.n = n
		#added.scaling = [var.xScale * var.xScale, 1, var.yScale * value]
		added.refresh()
		
	def close(self):
		self.shock.close()
		bge.logic.endGame()
		
	def run(self):
		try:
			(dataRaw, addr) = self.shock.recvfrom(var.buf)
			#data = loads(data)
			data = dataRaw.decode()
			l = simpleDecoder(data)
			cmd = l[0]
			
			try:
				if cmd == "addBlock":
					self.addBlock(float(l[2]), float(l[1]))
				if cmd == "setNScale":
					var.xScale = float(l[1])
					for block in self.blocks:
						block.refresh()
					self.x_adder.refresh()
				if cmd == "setValueScale":
					var.yScale = float(l[1])
					for block in self.blocks:
						block.refresh()
					self.y_adder.refresh()
				if cmd == "restart":
					bge.logic.restartGame()
				if cmd == "resetCamPos":
					self.cam.reset()
				if cmd == "setNDesc":
					self.nDeskripsi.text = l[1]
				if cmd == "setValueDesc":
					self.valueDeskripsi.text = l[1]
					
				print("Received message from {0}: ".format(str(addr)) + data)
				
				if cmd == "exit":
					print("exiting command from " + str(addr))
					bge.logic.endGame()
			except:
				checker.getInfo()
			
			
		except:
			#for now I'll have to bypass it :'v
			pass
			
class KX_CamPos(bge.types.KX_Camera):
	def __init__(self, old_owner):
		bge.render.setMousePosition(int(bge.render.getWindowWidth() / 2), int(bge.render.getWindowHeight() / 2))
		self.maxX = self["xMax"]
		self.maxY = self["yMax"]
		self.threshold = self['threshold']
		self.m = bge.logic.mouse
		self.speed = self['speed'] / bge.logic.getLogicTicRate()
		
		self.vek = Vector((0, 0, 0))
		
	def run(self):
		mpos = self.m.position
		moveTo = Vector((0, 0, 0))
		if mpos[0] < 1 - self.threshold:
			if self.vek.x > -self.maxX:
				self.vek.x -= self.speed
				moveTo.x = -self.speed
		if mpos[0] > self.threshold:
			if self.vek.x < self.maxX:
				self.vek.x += self.speed
				moveTo.x = self.speed
				
		self.applyMovement(moveTo, True)
		
	def reset(self):
		self.applyMovement(self.vek * -1, True)
		self.vek.x = 0
		self.vek.y = 0
		self.vek.z = 0
		bge.render.setMousePosition(int(bge.render.getWindowWidth() / 2), int(bge.render.getWindowHeight() / 2))
		
