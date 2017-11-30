#simple is better, this is badddd

class MathDojo(object):
	def __init__(self):
		self.num1 = num1 # this gets passed to add()/sub()
		self.nums = nums # this gets pased to checker()
		self.result = 0 # this is the final result
		self.checkNums = 0 # this takes the number in tuple or list and adds
		self.check1 = False # this is the check setting result to checkNums, in case both args are a list or a tuple
		self.check2 = False # this is the check for seeing which arg is an int and which is a list or tuple
		self.checkNum1 = False #num1 tuple or list? check it
		self.checkNums = False #nums tuple or list? check it		
		
	def checker(self):
		
		if type(self.nums) == list:
			self.CheckNums = True
			for num in self.nums:
				self.checkNums += num
				
		if type(self.nums) == tuple:
			self.CheckNums = True
			for num in self.nums:
				for tup in self.nums:
					self.checkNums += tup
							
		if type(self.num1) == list:
			self.CheckNums1 = True
			for numB in self.nums1:
				self.checkNums += numB
									
		if type(self.num1) == tuple:
			self.CheckNums1 = True
			for num in self.num1:
				for tup in self.num1:
					self.checkNums += tup
					
		if type(self.num1) and type(self.nums) == list:
			self.check1 = True
		
		if type(self.num1) and type(self.nums) == tuple:
			self.check1 = True
			
		if type(self.num1) or type(self.nums) == list:
			self.check2 = True
			
		if type(self.num1) or type(self.nums) == tuple:
			self.check2 = True			
			
		print 'The value of self.checkNums is ' + str(self.checkNums)
		return self
			
	def add(self, num1, *nums):
		self.checker()
		if self.check1 == True:
			self.result = self.checkNums
		if self.check2 == True:
			if self.CheckNums1 == True:
				self.result = self.nums + self.CheckNums	
			if self.CheckNums == True:
				self.result = self.num1 + self.CheckNums
		
		self.result += self.nums1 + self.checkNums
		return self
	
	def sub(self, num1, *nums):
		self.checker()
		
		if self.check2 == True:
			if self.CheckNums1 == True:
				self.result = self.nums - self.CheckNums	
			if self.CheckNums == True:
				self.result = self.num1 - self.CheckNums
				
		
calc = MathDojo()

calc.add(0,10)