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
	double_eps = False
	seq_length = 0
	
	if numbers.count(a) < 2:
		print "BOGUS"
		exit
	
	first_a = numbers.index(a)
	for i in range(first_a):
		numbers.pop(0)
	
	list_length = len(numbers)
	for i in range(list_length):
		
		seq_length = seq_length + 1
		if(numbers[i] == a) and i != 0:
			if numbers[i-1] != eps or double_eps == True:
				print "Accept", seq_length
				break
		
		if(numbers[i] == a) and i == 1:
			print "Accept", seq_length
			break
		
		double_eps = False
		
		if numbers[i] == eps and numbers[i-1] == eps:
			double_eps = True
		
		if i == list_length - 1:
			print "BOGUS"

detect_sequence(3, 7, nums)