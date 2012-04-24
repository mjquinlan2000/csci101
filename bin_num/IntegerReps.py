#!/usr/bin/env python
#Created by: Mike Quinlan
#Converts numbers to binary strings and binary strings to numbers
#This will actually return binary strings with the MSB first

import math

def decimal_value(bin_list, outval, base):
	if len(bin_list) == 0:
		return outval
	
	#Assuming the value is MSB first
	bin_list.reverse()
	if bin_list[0] == 1:
		outval = outval + base
	bin_list.pop(0)
	bin_list.reverse()
	return decimal_value(bin_list, outval, base*2)
	
			

def binary_bits(int_value, out_list):
	if int_value == 0:
		if len(out_list) == 0:
			return [0]
		else:
			out_list.reverse()
			return out_list
	out_list.append(int_value % 2)
	return binary_bits(int_value/2, out_list)

def check_input(num):
	try:
		num = int(num)
		if num < 0:
			return False
		return True
	except ValueError:
		return False
		
uinput = "junk"

while not check_input(uinput):
	uinput = raw_input("Please enter a positive integer greater than or equal to zero: ")

num = int(uinput)
print "You entered a", num
bin_list = binary_bits(num, list())
print "The binary representation (MSB first), is", bin_list
check_val = decimal_value(bin_list, 0, 1)
print "The double-check value is", check_val
