def check_score(score):
	if score < 0 or score > 100:
		return False
	return True

name = raw_input("What is your name?\n")

titles = ['Final Exam', 'Exam I', 'Exam II', 'Programming and Written Assignments', 'Quizzes', 'Group score on Quizzes']

total_score = 0
scores = dict()
weights = dict()

weights['Final Exam'] = 25
weights['Exam I'] = 15
weights['Exam II'] = 20
weights['Programming and Written Assignments'] = 16
weights['Quizzes'] = 12
weights['Group score on Quizzes'] = 12

for title in titles:
	score = -1
	while check_score(score) == False:
		score = input("What is your " + title + " Grade?\n")
	scores[title] = score
	
	total_score += (score/100.0)*weights[title]

print str(total_score) + " Percent"
