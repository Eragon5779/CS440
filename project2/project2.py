from random import randint
from time import sleep

t = 0
class Person:
	def __init__(self,uid):
		self.leave_time = 0
		self.in_time = randint(3,7)
		self.uid = uid
		if randint(1,10) >= 6:
			self.gender = 1
		else:
			self.gender = 0

line = []
bathroom = []

# utility function to pop and get proper time
def person_pop():
	p = line.pop()
	p.leave_time = t + p.in_time
	return(p)
def person_remove(d):
	try:
		i = line.index(d)
		p = line.pop(i)
		p.leave_time = t + p.in_time
		return(p)
	except:
		print("this shouldn't happen")
		return(Person(20))

def bLeave():
	if not bathroom:
		return
	for f in bathroom:
		if f.leave_time - t <= 0:
			print(str(f.uid) + " leaves the bathroom.")
			bathroom.remove(f)

def bCheck():
	try:
		initial_check = line[-3:]
	except:
		initial_check = line

	# state A
	if len(bathroom) == 0:
		bathroom.append(person_pop())
		print("Person " + str(bathroom[0].uid) + " enters the bathroom for " + str(bathroom[0].in_time))

		for f in initial_check[:2]:
			if f.gender == bathroom[0].gender:
				print("Person " + str(f.uid) + " enters the bathroom for " + str(f.in_time))
				bathroom.append(person_remove(f))

	# state B
	elif len(bathroom) == 1:
		for f in line:
			if len(bathroom) == 2:
				return
			elif f.gender == bathroom[0].gender:
				print("Person " + str(f.uid) + " enters the bathroom for " + str(f.in_time))
				bathroom.append(person_remove(f))

	# state C
	elif len(bathroom) == 2:
		return

	# state D
	elif len(bathroom) == 3:
		return

for f in range(0,20):
	line.append(Person(f))

while line:
	sleep(0.1)
	bLeave()
	if len(bathroom) < 3:
		bCheck()
	t += 1
