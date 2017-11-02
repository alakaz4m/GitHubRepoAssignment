my_info = {'name':'Michael','age': 19,'country_of_birth':'Honduras','fav_lang':'Python'}

for i in my_info.itervalues():
	if i == 'Michael':
		print 'My name is',i
	elif type(i) == int:
		print 'My age is',i
	elif i == 'Honduras':
		print 'My country of birth is',i
	elif i == 'Python':
		print 'My favorite language is',i
