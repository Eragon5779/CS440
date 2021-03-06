from random import randint

### state

# time, departed count
t = 0
dep = 0
line = []
bathroom = []
# class
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

### functions

## utility

# pop next in line
def person_pop():
	p = line.pop(0)
	p.leave_time = t + p.in_time
	return(p)
# pop specified person
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
def print_person(uid,g,i):
	print("Time: %2.0f; Person %2.0f (%s) enters the bathroom for %d minutes" % (t, uid, ("M" if g else "F"), i))

## main

# add to bathroom
def Arrive():
	# find last three items on list, or less if it's too small

	global line
	global bathroom
	add_bathroom = []

	if len(bathroom) == 0:
		p = person_pop()
		bathroom.append(p)
		print_person(p.uid + 1, p.gender, p.in_time)
	elif len(bathroom) == 2 and line[0].gender != bathroom[0].gender:
		return

	for f in line:
		index = line.index(f)
		if f.gender == bathroom[0].gender and index < 2 and len(bathroom) < 2:
			p = line[index]
			p.leave_time = t + p.in_time
			add_bathroom.append(line[index])
			print_person(line[index].uid + 1, line[index].gender, line[index].in_time)
		if f.gender == bathroom[0].gender and len(add_bathroom) < 1:
			p = line[index]
			p.leave_time = t + p.in_time
			add_bathroom.append(line[index])
			print_person(line[index].uid + 1, line[index].gender, line[index].in_time)

	line = [f for f in line if f not in add_bathroom]
	bathroom += add_bathroom

# finds those who are done and removes
def UseFacilities():
	# if it's empty
	if not bathroom:
		return
	# if it's not, iterate over every person in there
	for f in bathroom:
		# check if current time is past/equal to their leave time
		if f.leave_time - t <= 0:
			# print(str(f.uid) + " leaves the bathroom.")
			global dep
			dep += 1
			print("Time: %2.0f; Person %2.0f (%s) exits (departure = %2.0f)" % (t, f.uid + 1, ("M" if f.gender else "F"), dep))
			Depart(f)

# removes specified person from bathroom
def Depart(f):
	bathroom.remove(f)

### main

# 3 required cases
case = input("Input case (a,b,c): ")

# 5 at a time
if case.lower() == 'a':
	# count of total people
	c = 0
	# first 5 added
	for f in range(0,5):
		line.append(Person(f))
		print("Time: %2.0f; Person %2.0f (%s) arrives" % (t, f + 1, ("M" if line[f].gender else "F")))
		c += 1

	# central while loop, until count hits 20 and line empties
	while dep < 20:
		# adds 5 more at times
		if t == 10:
			print("\n 5 new arrivals \n")
			for f in range(0,5):
				temp = Person(f + 5)
				line.append(temp)
				print("Time: %2.0f; Person %2.0f (%s) arrives" % (t, temp.uid + 1, ("M" if temp.gender else "F")))
				c += 1
		elif t == 20:	
			print("\n 5 new arrivals \n")
			for f in range(0,5):
				temp = Person(f + 10)
				line.append(temp)
				print("Time: %2.0f; Person %2.0f (%s) arrives" % (t, temp.uid + 1, ("M" if temp.gender else "F")))
				c += 1
		elif t == 30:
			print("\n 5 new arrivals \n")
			for f in range(0,5):
				temp = Person(f + 15)
				line.append(temp)
				print("Time: %2.0f; Person %2.0f (%s) arrives" % (t, temp.uid + 1, ("M" if temp.gender else "F")))
				c += 1

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
		print("Time: %2.0f; Person %2.0f (%s) arrives" % (t, f + 1, ("M" if line[f].gender else "F")))
		c += 1

	# central while loop, until count hits 20 and line empties
	while dep < 20:
		# adds 10 more at times
		if t == 10:
			print("\n 10 new arrivals \n")
			for f in range(0,10):
				temp = Person(f + 10)
				line.append(temp)
				print("Time: %2.0f; Person %2.0f (%s) arrives" % (t, temp.uid + 1, ("M" if temp.gender else "F")))
				c += 1

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
		print("Time: %2.0f; Person %2.0f (%s) arrives" % (t, f + 1, ("M" if line[f].gender else "F")))

	# main while loop
	while dep < 20:
		# remove from bathroom
		UseFacilities()
		# add to bathroom
		if len(bathroom) < 3 and line:
			Arrive()
		# increment time
		t += 1

# improper input
else:
	print("invalid input")

for f in bathroom :
	print(f.uid)
