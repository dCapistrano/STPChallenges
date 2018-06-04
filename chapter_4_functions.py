def squared_func(x):
	""" Takes an int and returns it multiplied by 2.
	:param x: int.
	:return: x multiplied by 2
	"""
	return int(x**2)



def string_func(x):
	""" Prints string passed into it.
	:param string: str.
	"""
	print(x)



def some_func(x, y, z, a=100, b=100):
	""" Returns the result of adding 3 required params
	and 2 optional params.
	:param x: int.
	:param y: int.
	:param z: int.
	:param a: int.
	:param b: int.
	:return: int.
	"""
	return x + y + z + a + b



def divide(x):
	""" Accepts param and divides it by 2.
	:return: int.
	"""
	return x / 2

def multiply(y):
	""" Accepts param and multiplies it by 4.
	:return: int.
	"""
	return y * 4



def convert(string):
	""" Converts passed in str to int.
	:param string: str.
	:return: string converted to int.
	"""
	try:
		return float(string)
	except (ValueError):
		print("wrong value")



			