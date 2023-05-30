def is_odd(x):
	"""
	Return True if integer is odd
	Return False if integer is not odd
	Raise TypeError if x is not an integer
	"""
	if not isinstance(x, int):
		raise TypeError("'x' must be an integer")
	return	

assert is_odd.__doc__ is not None

number=False
try:
	is_odd('sdfsdfwerw')
except TypeError:
	number=True
assert(number)	

