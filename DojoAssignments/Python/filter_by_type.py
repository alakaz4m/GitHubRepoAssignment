my_input = input('Enter anything: ')
print type(my_input)
if type(my_input) == str:
	if len(my_input) >= 50:
		print "Long sentence"
	else:
		print "Short sentence"
	
	
if type(my_input) == int:
	if my_input >= 100:
		print "That's a big number!"
	else:
		print "That's a small number"
		
		
if type(my_input) == list:
	if len(my_input) >= 10:
		print "That's a big list"
	else:
		print "That's a small list"
		