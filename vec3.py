import math 
import operator

class Vec3:
	def __init__(self, x, y, z):
		self.vals = [x,y,z]

	def x(self):
		return self.vals[0]

	def y(self):
		return self.vals[1]

	def z(self):
		return self.vals[2]

	def r(self):
		return self.vals[0]

	def g(self):
		return self.vals[1]

	def b(self):
		return self.vals[2]

	def length(self):
		return math.sqrt(self.x()*self.x() + self.y()*self.y() + self.z()*self.z())

	def length_squared(self):
		return self.x()*self.x() + self.y()*self.y() + self.z()*self.z()

	def unit_vector(self):
		return self / self.length()

	def dot(self, vec):
		return self.x()*vec.x() + self.y()*vec.y() + self.z()*vec.z()

	def cross(self, vec):
		return Vec3(self.y()*vec.z() - self.z()*vec.y(),
					self.z()*vec.x() - self.x()*vec.z(),
					self.x()*vec.y() - self.y()*vec.x())

	def __neg__(self):
		return Vec3(-self.x(), -self.y(), -self.z())

	def __pos__(self):
		return self

	def __abs__(self):
		return self.length()

	def __add__(self, vec):
		return Vec3(self.x() + vec.x(), self.y() + vec.y(), self.z() + vec.z())

	def __sub__(self, vec):
		return Vec3(self.x() - vec.x(), self.y() - vec.y(), self.z() - vec.z())

	def __mul__(self, vec):
		if isinstance(vec, Vec3):
			return Vec3(self.x() * vec.x(), self.y() * vec.y(), self.z() * vec.z())
		return Vec3(self.x() * vec, self.y() * vec, self.z() * vec) # scalar multiplication

	def __truediv__(self, vec):
		if isinstance(vec, Vec3):
			return Vec3(self.x() / vec.x(), self.y() / vec.y(), self.z() / vec.z())
		return Vec3(self.x() / vec, self.y() / vec, self.z() / vec) # scalar division

	def __str__(self):
		return str(self.x()) + " " + str(self.y()) + " " + str(self.z()) + "\n"

	def __repr__(self):
		return str(self.vals)