#!/usr/bin/python 

class Vector:
	"""Sum of vectors"""
	def __init__(self, a, b):
		self.a = a
		self.b = b

	def __str__(self):
		return "Vector(%d, %d)" % (self.a, self.b)

	def __add__(self, other):
		return Vector( self.a + other.a, self.b + other.b )


v1 = Vector(4, -5)
v2 = Vector(5, 6)

print v1 + v2
