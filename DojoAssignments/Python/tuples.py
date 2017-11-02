my_dict = {
  "Speros": "(555) 555-5555",
  "Michael": "(999) 999-9999",
  "Jay": "(777) 777-7777"
}

my_list = []

def tup_out(my_dict):
	for index in my_dict.iteritems():
		my_list.append(index)
	print my_list
		
		
		
		
tup_out(my_dict)