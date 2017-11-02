import random

print "Scores and Grades"
for i in range(0,11):
	random_num = random.randint(0,100)
	if random_num in range(90,100):
		print "Score: " , random_num , "; Your grade is A"
	elif random_num in range(80,89):
		print "Score: " , random_num , "; Your grade is B"
	elif random_num in range(70,79):
		print "Score: " , random_num , "; Your grade is C"
	elif random_num in range(60,69):
		print "Score: " , random_num , "; Your grade is D"
	elif random_num in range(0,59):
		print "Score: " , random_num , "; Dude, study next time.."
		