class Rectangle(Shape):
	def __init__(self, width, length):
		self.width = width
		self.length = length
	def calculate_perimeter(self):
		return self.width * 2 + self.length * 2

class Square(Shape):
	def __init__(self, s1):
		self.s1 = s1
	def calculate_perimeter(self):
		return self.s1 * 4
	def change_size(self, new_size):
		self.s1 += new_size

"""challenge 3"""
class Shape():
	def what_am_i(self):
		print("I am a shape")



"""challenge 4"""
class Horse():
	def __init__(self, name):
		self.name = name

class Rider():
	def __init__(self, name, horse):
		self.name = name		
		self.horse = horse
		




