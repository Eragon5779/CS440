import threading
import time

class Person:
	
	def __init__(self, ID, gender, time):
		self.ID = ID
		self.gender = gender
		self.time = time
		
	def Arrive(self) :
		pass
	
	def UseFacilities(self) :
		pass
	
	def Depart(self) :
		pass
	
class OnePerson(threading.Thread):
	def __init__(self, threadID, p) :
		self.threadID = threadID
		self.p = p
	def run(self):
		p.Arrive()
		p.UseFacilities()
		p.Depart()
	
queue = []
inLine = []
