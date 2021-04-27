import math
import operator

class Point:
	def __init__(self, x, y):
		self.x = x
		self.y = y
	def __repr__(self):
		return 'Point({},{})'.format(self.x, self.y)
	def distance(self, x, y):
		return math.hypot(self.x -x, self.y -y)

if __name__ == '__main__':
	p = Point(2,3)
	print(p)
	d = getattr(p, 'distance')(0,0)
	print(d)
	d = operator.methodcaller('distance', 0, 0)(p)
	print(d)
