class Animal(object):
	def __init__(self, name, health):
		self.name = name
		self.health = health
		
	def walk(self):
		print 'Action: Walking...'
		self.health -= 1
		return self
		
	def run(self):
		print 'Action: Running...'
		self.health -= 5
		return self
		
	def displayHealth(self):
			print self.health
			
class Dog(Animal):
	def __init__(self, name, health):
		super(Dog, self).__init__(name, health)
		
		self.health = 150
		
	def pet(self):
		print 'Action: Petting...'
		self.health = self.health + 5
		return self

	
class Dragon(Animal):
	def __init__(self, name, health):
		super(Dragon, self).__init__(name, health)
		
		self.health = 170
	def fly(self):
		print 'Action: Flying...'
		self.health = self.health - 10
		return self
		
	def displayHealth(self):
		print 'This is a dragon!'
		super(Dragon, self).displayHealth()
		
		
Bear = Animal('Tofu', 100)
Doge = Dog('Coco', 150)
Draco = Dragon('Draco', 170)

Bear.walk().walk().walk().run().run()
Bear.displayHealth()

Doge.walk().walk().walk().run().run().pet()
Doge.displayHealth()

#Draco.displayHealth()

#Chicken = Animal('Bawk', 100) --------- This is to check that Animal class doesn't use Dragon and Dog methods
#
#Chicken.pet()
#Chicken.fly()
#Chicken.displayHealth()
