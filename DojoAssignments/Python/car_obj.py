import random

class Car(object):
	def __init__(self,given_price):
		self.price = given_price
		self.max_speed = random.randint(100,200)
		self.fuel = random.randint(10,100)
		self.mileage = random.randint(1000,10000)
		self.tax = 0
		
	def taxPrice(self):
		if self.price >= 10000:
			self.tax = 0.15
		else:
			self.tax = 0.12
		return self
	
	def display_all(self):
		print('.:Car Information:.')
		print('Price:', str(self.price))
		print('Speed:', str(self.max_speed))
		print('Fuel:',str(self.fuel))
		print('Mileage:',str(self.mileage))
		print('Tax:',str(self.tax))
		return self
	
redCar = Car(10000)
blueCar = Car(5000)
greenCar = Car(1000)
orangeCar = Car(50000)
goldCar = Car(100000)
yellowCar = Car(12000)

redCar.taxPrice().display_all()
blueCar.taxPrice().display_all()
greenCar.taxPrice().display_all()
orangeCar.taxPrice().display_all()
goldCar.taxPrice().display_all()
yellowCar.taxPrice().display_all()