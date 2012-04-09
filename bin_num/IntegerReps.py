#!/usr/bin/env python
#Created by: Mike Quinlan
#Converts numbers to binary strings and binary strings to numbers
#This will actually return binary strings with the MSB first

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
			return out_list.reverse()
	print int_value, int_value%2, int_value/2
	out_list.append(int_value % 2)
	return binary_bits(int_value/2, out_list)

bin_list = [1,0,1,1,0]

x = decimal_value(bin_list, 0, 1)

aList = binary_bits(x, list())

print x, aList
