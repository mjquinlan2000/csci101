#!/usr/bin/env python
#Created By: Mike Quinlan

lines = list()
nums = list()

with open("sequence.txt") as file:
	lines = file.readlines()

for line in lines:
	try:
		nums.append(int(line))
	except ValueError:
		print "NOT A VALID INPUT: " + line.rstrip('\n')
		exit

def detect_sequence(a, eps, numbers):
	if numbers.count(a) < 2:
		print "BOGUS"
		exit
	
	first_a = numbers.index(a)
	for i in range(first_a):
		numbers.pop(0)
	print numbers

detect_sequence(3, 7, nums)