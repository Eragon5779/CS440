from random import randint
from time import sleep

# main time var
t = 0
# main depart var
d = 0

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
	# try catch in case of empty line, should never occur
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

# depart, usefacilities, and arrive

# removes specified bathroom user
def Depart(f):
	bathroom.remove(f)

# finds those who are done and removes
def UseFacilities():
	# if it's empty
	if not bathroom:
		return
	# if it's not, iterate over every person in there
	for f in bathroom:
		# check if current time is past/equal to their leave time
		if f.leave_time - t <= 0:
			print(str(f.uid) + " leaves the bathroom.")
			Depart(f)

# finds compatible people in line and puts them in bathroom
def Arrive():
	# find last three items on list, or less if it's too small

	# state A: empty
	if len(bathroom) == 0:
		# initalize first person
		bathroom.append(person_pop())
		# get other 2 people to check
		try:
			initial_check = line[-2:]
		except:
			initial_check = line

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
			# if it's 2 big, check if next is addable to transition to State D
			if len(bathroom) == 2 and line[-1].gender == bathroom[0].gender:
				bathroom.append(person_pop())
			elif len(bathroom) == 3:
				return
			# else, find a compatible person and add
			elif f.gender == bathroom[0].gender:
				print("Person " + str(f.uid) + " enters the bathroom for " + str(f.in_time))
				bathroom.append(person_remove(f))

	# state C: 2 people in
	elif len(bathroom) == 2:
		if line[-1].gender == bathroom[0].gender:
			bathroom.append(person_pop())
		else:
			return

	# state D: 3 people in
	elif len(bathroom) == 3:
		return

# 3 required cases
case = input("Input case (a,b,c): ")

# 5 at a time
if case.lower() == 'a':
	# count of total people
	c = 0
	# first 5 added
	for f in range(0,5):
		line.append(Person(f))
		print("Time: %d; Person %d (%s) arrives" % (t, f, ("M" if line[f].gender else "F")))
		c += 1

	# central while loop, until count hits 20 and line empties
	while c < 20 or line:
		# adds 5 more at times
		if t == 10:
			print("\n 5 new arrivals \n")
			for f in range(0,5):
				temp = Person(f + 5)
				line.append(temp)
				print("Time: %d; Person %d (%s) arrives" % (t, f + 5, ("M" if temp.gender else "F")))
				c += 1
		elif t == 20:	
			print("\n 5 new arrivals \n")
			for f in range(0,5):
				temp = Person(f + 10)
				line.append(temp)
				print("Time: %d; Person %d (%s) arrives" % (t, f + 10, ("M" if temp.gender else "F")))
				c += 1
		elif t == 30:
			print("\n 5 new arrivals \n")
			for f in range(0,5):
				temp = Person(f + 15)
				line.append(temp)
				print("Time: %d; Person %d (%s) arrives" % (t, f + 15, ("M" if temp.gender else "F")))
				c += 1

		# sleep for readability
		sleep(0.1)
		# remove from bathroom
		UseFacilities()
		# add to bathroom
		if len(bathroom) < 3 and line:
			Arrive()
		# increment time
		t += 1

# 10 at a time
elif case.lower() == 'b':
	# count of total people
	c = 0
	# first 10 added
	for f in range(0,10):
		line.append(Person(f))
		print("Time: %d; Person %d (%s) arrives" % (t, f, ("M" if line[f].gender else "F")))
		c += 1

	# central while loop, until count hits 20 and line empties
	while c < 20 or line:
		# adds 10 more at times
		if t == 10:
			print("\n 10 new arrivals \n")
			for f in range(0,10):
				temp = Person(f + 10)
				line.append(temp)
				print("Time: %d; Person %d (%s) arrives" % (t, f + 10, ("M" if temp.gender else "F")))
				c += 1

		# sleep for readability
		sleep(0.1)
		# remove from bathroom
		UseFacilities()
		# add to bathroom
		if len(bathroom) < 3 and line:
			Arrive()
		# increment time
		t += 1

# all at once
elif case.lower() == 'c':
	# line generation
	for f in range(0,20):
		line.append(Person(f))
		print("Time: %d; Person %d (%s) arrives" % (t, f, ("M" if line[f].gender else "F")))

	# main while loop
	while line:
		# sleep for readability
		sleep(0.1)
		# remove from bathroom
		UseFacilities()
		# add to bathroom
		if len(bathroom) < 3:
			Arrive()
		# increment time
		t += 1

# improper input
else:
	print("invalid input")
