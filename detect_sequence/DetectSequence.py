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
	is_sequence = False
	
	if numbers.count(a) < 2 or len(numbers) == 0:
		print "BOGUS"
		exit
	
	first_a = numbers.index(a)
	for i in range(first_a):
		numbers.pop(0)
	
	while not is_sequence and len(numbers) > 0:
		if numbers[0] == a:
			print "Something"
		elif numbers[0] == eps:
			if numbers[1] == a:
				numbers.pop(0)
		else:
			print "One last thing"
		numbers.pop(0)

detect_sequence(3, 7, nums)