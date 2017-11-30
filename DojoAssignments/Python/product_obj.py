import random

class ProductSys(object):
	def __init__(self, item_name,price, tax):
		self.item = item_name
		self.tax = tax
		self.price = float(price) * float(tax)
		self.brand = 'Kraft'
		self.weight = random.randint(1,30)
		self.sold = False
		self.returnItm = False
		self.status = '[FOR SALE]'
		self.used = False
		self.inBox = False
		
	
	def updateStatus(self):
		if self.sold == False:
			self.status = '[FOR SALE]'
		if self.sold == True:
			self.status == '[SOLD]'
		if self.returnItm == True:
			self.status = '[RETURNED]'
		if self.used == True:
			self.status = '[USED]'
		return self
		
		
	def displayInfo(self):
		self.updateStatus()
		print '##############################'
		print 'Item: ' + self.item
		print 'Price: $' + str(self.price)
		print 'Brand: ' + self.brand
		print 'Weight: ' + str(self.weight) + 'oz'
		print 'Status: ' , self.status
		print '##############################'
		
		
	def returnItem(self, reason, inBox):
		if reason == 'defective':
			print self.price
			self.price = 0.0
			self.returnItm = True
		else:
			if reason == 'like new':
				self.used = True
				if inBox == True:
					self.discount = (float(self.price) * 0.20)
					self.price = self.price - self.discount
			self.updateStatus()
		return self
		
item2 = ProductSys('Can of Beans', 200,1.07)

item2.displayInfo()
item2.returnItem('defective', True)
item2.displayInfo()