"""challenge 1 & 2"""
class Square(Shape):
	square_list = []
	def __init__(self, s1):
		self.s1 = s1
	def calculate_perimeter(self):
		return self.s1 * 4
	def change_size(self, new_size):
		self.s1 += new_size
	def __repr__(self):
		return "{} by {} by {} by {}".format(self.s1, self.s1, self.s1, self.s1)

class Shape():
	def what_am_i(self):
		print("I am a shape")



"""challenge 3"""		
def compare(obj1, obj2):
	return obj1 is obj2