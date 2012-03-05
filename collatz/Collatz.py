#!/usr/bin/env python
#Created By: Mike Quinlan
#Displays a hailstone sequence from a positive integer inputted by a user

uinput = input("Enter a positive integer value: ")

def hailstone_seq(n, outstr):
	if n == 1:
		outstr += str(n)
		return outstr
	
	if n % 2 == 0:
		outstr += str(n) + " "
		return hailstone_seq(n/2, outstr)
	else:
		outstr += str(n) + " "
		return hailstone_seq(3*n + 1, outstr)
	
	

outstr = hailstone_seq(uinput, "")
print outstr