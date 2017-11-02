li = ['magical unicorns',19,'hello',98.98,'world']
#li = [2,3,1,7,4,12]
#li = ['magical','unicorns']


num = []
string = ""
sum1 = 0
for i in li:
	if type(i) == str:
#		print "The list you entered is of string type"
#		print "".join(i)
		string += " " + i
		
	if type(i) == int:
#		print "The list you entered is of integer type"
		sum1 += i

if len(string) > 0 and sum1 > 0:
	print "The list you entered is of mixed type"
elif sum1 == 0:
	print "The list you entered is of string type"
else:
	print "The list you entered is of integer type"