def odd_even():
	for i in range(1,2001):
		if i % 2 == 0:
			print "Number is " + str(i) + ". This is an even number."
		else:
			print "Number is " + str(i) + ". This is an odd number."

new_list = []
my_list = [1,2,3]
count_list = []
def multiply(my_list, num):
	for i in my_list:
		new_list.append(i*num)
	return new_list
		
#multiply(my_list, 3)
#print new_list

def layered_multiples(new_list):
	print new_list
	for x in new_list:
		newest_list = []
		for y in range(0,x):
			newest_list.append(1)
		count_list.append(newest_list)
	return count_list
answer = layered_multiples(multiply(my_list, 3))
print answer