import random
heads = 0
tails = 0

print 'Starting the program...'
for i in range(1,5001):
	coin = random.randint(0,1)
	if coin == 0:
		heads += 1
		result = 'head'
	elif coin == 1:
		tails += 1
		result = 'tails'
	print "Attemp #" , i , ": Throwing a coin... It's a" , result + '! ... Got' , heads , 'head(s) so far and' , tails , 'tail(s) so far'