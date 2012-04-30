#!/usr/bin/env python
#Created By: Mike Quinlan

a = -1
begin = -1
end = -1

def check_a(a):
	try:
		a = int(a)
		if(a % 2 != 1 or a < 1):
			return False
		else:
			return True
	except ValueError:
		return False

def check_range_value(value):
	try:
		value = int(value)
		if(value < 1):
			return False
		else:
			return True
	except ValueError:
		return False

while not check_a(a):
	a = raw_input("Enter a positive integer value for the 3*x+a rule when x is odd: ")

while not check_range_value(begin):
	begin = raw_input("Enter the beginning of the range to search (s>0): ")

a, begin = int(a), int(begin)

while end < begin:
	while not check_range_value(end):
		end = raw_input("Enter the end range to search (t>s): ")
	end = int(end)
	if(end < begin):
		print "The end of the range must be larger than the beginning"
		end = -1

