def draw_stars(x):
	for i in x:
		fancy = ""
		length = i
		boolean = True
		if type(i) != int:
			length = len(i)
			boolean = False
		for y in range(0,length):
			if boolean == False:
				fancy = [i][0][0] * length
			else:
				fancy = '*' * length
		print fancy
		
x = [2,'chicken','taco',6,3,1]
draw_stars(x)