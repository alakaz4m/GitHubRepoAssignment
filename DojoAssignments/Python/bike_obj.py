class Bike(object):
	def __init__(self,given_price,max_speed):
		self.price = given_price
		self.max_speed = max_speed
		self.miles = 0.0
	
	def displayInfo(self):
		print('#######################################')
		print('## Bike Info ##')
		print('Price:' , self.price)
		print('Speed:' , self.max_speed)
		print('Total miles:',self.miles)
		print('#######################################')

		return self
	
	def ride(self):
		print('#######################################')
		print('########         Riding         #######')
		print('Riding..Total miles:',self.miles)
		self.miles += 10.0
		print('Done riding....Total miles:',self.miles)
		return self
	
	def reverse(self):
		print('#######################################')
		print('########         Reversing     ########')
		if self.miles < 5:
			self.miles = 0
		else:
			self.miles -= 5.0
		print('Reversing..Total miles:',self.miles)
		return self
	

greenBike = Bike(200,25)
redBike = Bike(300,30)
blueBike = Bike(50,10)

for i in range(0,4):
	greenBike.ride()

greenBike.reverse().displayInfo()

for x in range(0,3):
	redBike.ride().reverse()
	
redBike.displayInfo()

for y in range(0,4):
	blueBike.reverse()

blueBike.displayInfo()