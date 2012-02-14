def check_score(score):
	if score < 0 or score > 100:
		return False
	return True

name = raw_input("What is your name?\n")

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
		score = input("What is your " + title + " Grade?\n")
	
	total_score += (score/100.0)*weights[title]

print name + ", your current course grade is", str(total_score) + "%"
