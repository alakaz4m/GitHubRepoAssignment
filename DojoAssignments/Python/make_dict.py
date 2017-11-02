name = ["Anna", "Eli", "Pariece", "Brendan", "Amy", "Shane", "Oscar"]
favorite_animal = ["horse", "cat", "spider", "giraffe", "ticks", "dolphins", "llamas"]

def make_dict(arr1,arr2):
	new_dict = {}
	if len(arr1) >= len(arr2):
		new_zip = zip(arr1,arr2)
		new_dict = new_zip
	else:
		new_zip = zip(arr2,arr1)
		new_dict = new_zip
	print new_dict
	
	
make_dict(name,favorite_animal)