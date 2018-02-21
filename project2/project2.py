from random import randint
from time import sleep

# main time var
t = 0

class Person:
	def __init__(self,uid):
		# init'd to 0, will change later
		self.leave_time = 0
		# rng for how long they stay
		self.in_time = randint(3,7)
		self.uid = uid
		# weighted rng for gender
		if randint(1,10) >= 6:
			self.gender = 1
		else:
			self.gender = 0

# empty line and bathroom variables
line = []
bathroom = []

# utility function to pop and get proper time
def person_pop():
	p = line.pop()
	p.leave_time = t + p.in_time
	return(p)
def person_remove(d):
	# try catch in case of empty line
	try:
		i = line.index(d)
		p = line.pop(i)
		p.leave_time = t + p.in_time
		return(p)
	except:
		print("\n Unexpected happenings")
		print(d.uid)
		print(line)
		print("")

# leave/check; each loop, both are called

# leave removes those who are done
def bLeave():
	# if it's empty
	if not bathroom:
		return
	# if it's not, iterate over every person in there
	for f in bathroom:
		# check if current time is past/equal to their leave time
		if f.leave_time - t <= 0:
			print(str(f.uid) + " leaves the bathroom.")
			bathroom.remove(f)

# check finds compatible people in line
def bCheck():
	# find last three items on list, or less if it's too small
	try:
		initial_check = line[-3:]
	except:
		initial_check = line

	# state A: empty
	if len(bathroom) == 0:
		# initalize first person
		initial_check.remove(line[-1])
		bathroom.append(person_pop())
		print("Person " + str(bathroom[0].uid) + " enters the bathroom for " + str(bathroom[0].in_time))

		# check the next 2 for compatible people
		for f in initial_check:
			# if gender matches
			if f.gender == bathroom[0].gender:
				# add them to bathroom
				print("Person " + str(f.uid) + " enters the bathroom for " + str(f.in_time))
				bathroom.append(person_remove(f))

	# state B: 1 person in
	elif len(bathroom) == 1:
		# for each in line
		for f in line:
			# if it's 2 big, return
			if len(bathroom) == 2:
				return
			# else, find a compatible person and add
			elif f.gender == bathroom[0].gender:
				print("Person " + str(f.uid) + " enters the bathroom for " + str(f.in_time))
				bathroom.append(person_remove(f))

	# state C: 2 people in
	elif len(bathroom) == 2:
		return

	# state D: 3 people in
	elif len(bathroom) == 3:
		return

case = input("Input case (a,b,c): ")

if case.lower() == 'a':
	c = 0
	for f in range(0,5):
		line.append(Person(f))
		c += 1

	while c < 20 or line:
		if t == 10:
			print("\n 5 new arrivals \n")
			for f in range(0,5):
				line.append(Person(f + 5))
				c += 1
		elif t == 20:	
			print("\n 5 new arrivals \n")
			for f in range(0,5):
				line.append(Person(f + 10))
				c += 1
		elif t == 30:
			print("\n 5 new arrivals \n")
			for f in range(0,5):
				line.append(Person(f + 15))
				c += 1

		sleep(0.1)
		bLeave()
		if len(bathroom) < 3 and line:
			bCheck()
		t += 1

elif case.lower() == 'b':
	c = 0
	for f in range(0,10):
		line.append(Person(f))
		c += 1

	while c < 20 or line:
		if t == 10:
			print("\n 10 new arrivals \n")
			for f in range(0,10):
				line.append(Person(f))
				c += 1

		sleep(0.1)
		bLeave()
		if len(bathroom) < 3 and line:
			bCheck()
		t += 1

elif case.lower() == 'c':
	# line generation
	for f in range(0,20):
		line.append(Person(f))

	# main while loop
	while line:
		# sleep for readable output
		sleep(0.1)
		# leave/check
		bLeave()
		if len(bathroom) < 3:
			bCheck()
		# time increment
		t += 1

else:
	print("invalid input")
