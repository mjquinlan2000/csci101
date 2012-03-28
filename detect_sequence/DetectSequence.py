#!/usr/bin/env python
#Created By: Mike Quinlan

with open("sequence.txt") as file:
	lines = file.readlines()

for line in lines:
	line = int(line)
	print line