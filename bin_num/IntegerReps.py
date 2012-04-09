#!/usr/bin/env python
#Created by: Mike Quinlan
#Converts numbers to binary strings and binary strings to numbers
#This will actually return binary strings with the MSB first

def decimal_value(bin_list, outval, base):
	if len(bin_list) == 0:
		return outval
	
	#Assuming the value is MSB first
	bin_list.reverse()
	if bin_list[0] == '1':
		outval = outval + base
	bin_list.pop(0)
	bin_list.reverse()
	decimal_value(bin_list, outval, base*2)
	
			

def binary_bits(int_value):
