#!/usr/bin/env python
#Created By: Mike Quinlan
#Determines the total course grade percentage for csci101 courses based on the syllabus
#Also logs them into a file specified by the user

def check_score(score):
	if score < 0 or score > 100:
		return False
	return True
	
fname = raw_input("What is the name of the log file?\n")

name = raw_input("What is your name?\n")

logline = "Student Name:{0}\t".format(name)

total_score = 0
weights = dict()

weights['Final Exam'] = 25
weights['Exam I'] = 15
weights['Exam II'] = 20
weights['Programming and Written Assignments'] = 16
weights['Quizzes'] = 12
weights['Median group score on Quizzes'] = 12

for title in weights.keys():
	score = -1
	while check_score(score) == False:
		score = input("What is your {0} Grade? (0 to 100 inclusive)\n".format(title))
		
	current_score = (score/100.0)*weights[title]
	
	logline += "{0}:{1:.2f}\t".format(title, score)
	
	total_score += current_score

logline += "Course Grade:{0:.2f}\n".format(total_score)

#The 'with' keyword allows for the file to be automatically closed when the block of code
#terminates or an exception is raised. This gets rid of try-finally blocks and removes
#all locks from the file upon a failure of the script. Therefore, logfile.close() is not
#needed in this case
with open(fname, "a") as logfile:
	logfile.write(logline)

print "{0}, your current course grade is {1:.2f}%".format(name, total_score)
