import statistics

statistics.mean([1,3,4,123,32,4])



"""module1 named cubed.py"""
def cube_it(x):
	return x ** x

"""module2"""
import cubed

result = cubed.cubed(3)
print(result)