print '################'
print 'Find and Replace'
words = "It's thanksgiving day. It's my birthday too!"
print words.find('day')
new_string = words.replace('day', 'month')
print '################'
print 'Min and Max'


y = []
x = [2,54,True,'pizza',232,12]
for i in x:
	if type(i) == int:
		y.append(i)
print "The min is " + str(min(y))
print "The max is " + str(max(y))
print '################'
print 'First and Last'
x = ["hello",2,54,-2,7,12,98,"world"]
final = [x[0],x[-1]]
print final
print '################'
print 'New List'
y = [19,2,54,-2,7,12,98,32,10,-3,6]
y = sorted(y)
print y
b = y[len(y)/2:]
a = y[:len(y)/2]
print a
print b