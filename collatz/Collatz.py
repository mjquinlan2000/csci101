#!/usr/bin/env python
#Created By: Mike Quinlan
#Displays a hailstone sequence from a positive integer inputted by a user

#Global variables
increases = 0
decreases = 0

#Recursive Hailstone Sequence function
def hailstone_seq(n):
	global increases
	global decreases
	if n == 1:
		print str(n)
		return
	
	if n % 2 == 0:
		print str(n),
		increases += 1
		return hailstone_seq(n/2)
	else:
		print str(n),
		decreases += 1
		return hailstone_seq(3*n + 1)

#Input helper function
def check_input(n):
	try:
		n = int(n)
		if n < 1:
			return False
		else:
			return True
	
	except ValueError:
		return False

#Main body of code
uinput = -1

while not check_input(uinput):
	uinput = raw_input("Enter a positive integer value: ")

uinput = int(uinput)

hailstone_seq(uinput)
print "Hailstone sequence lenth for {0:d} is {1:d} with {2:d} increases and {3:d} decreases".format(uinput, increases + decreases + 1, increases, decreases)