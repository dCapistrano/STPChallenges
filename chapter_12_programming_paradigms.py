rock = []
country = []

def collect_songs():
	song = "Enter a song."
	ask = "Type r or c. q to quit: "
	while True:
		genre = input(ask)
		if genre == "q":
			break
		if genre == "r":
			rk = input(song)
			rock.append(rk)
		elif genre == ("c"):
			cy = input(song)
			country.append(cy)
		else:
			print("Invalid.")
	print(rock)
	print(country)

collect_songs()



class Orange:
	def __init__(self, w, c):
		"""weights are in oz"""
		self.weight = w
		self.color = c
		self.mold = 0
		print("Created!")
	def rot(self, days, temp):
		self.mold = days * temp




class Rectangle():
	def __init__(self, w, l):
		self.width = w
		self.len = l
	def area(self):
		return self.width * self.len
	def change_size(self, w, l):
		self.width = w
		self.len = l



"""challenge 1"""
class Apple:
	def __init__(self, w, c, t, s):
		self.weight = w
		self.color = c
		self.type = t
		self.seeded = s



"""challenge 2"""
import math

class Circle:
	def __init__(self, r):
		self.radius = r
	def calc_area(self):
		return self.radius**2 * math.pi



"""challenge 3"""
class Triangle:
	def __init__(self, base, height):
		self.base = base
		self.height = height
	def calc_area(self):
		return (self.height * self.base) / 2



"""challenge 4"""
class Hexagon:
	def __init__(self, s1, s2, s3, s4, s5, s6):
		self.s1 = s1
		self.s2 = s2
		self.s3 = s3
		self.s4 = s4
		self.s5 = s5
		self.s6 = s6
	def calc_perimeter(self):
		return self.s1 + self.s2 + self.s3 + self.s4 + self.s5 + self.s6


		





















