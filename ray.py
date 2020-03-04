from vec3 import Vec3

class Ray:
	"""
	Represents 3d ray starting at point A poiting in direction of vector B.
	"""
	def __init__(self, v, w):
		self.A = v
		self.B = w

	def origin(self):
		return self.A

	def direction(self):
		return self.B

	def point_at_parameter(self, t):
		return self.A + self.B*t

	def __repr__(self):
		return "A: " + str(self.A) + "B: " + str(self.B)