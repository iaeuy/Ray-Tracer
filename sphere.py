
import math
from hitable import Hitable

class Sphere(Hitable):
	def __init__(self, center, radius, material = None):
		super().__init__()
		self.center = center
		self.radius = radius
		self.matrl = material

	def hit(self, r, t_min, t_max):
		"""
		If r = A + B*t then it hits the sphere when t satisfies
		dot(B,B)*t^2 + 2dot(B, A-C)*t + dot(A-C, A-C) - R^2 = 0
		"""
		shifted = r.origin() - self.center
		B = r.direction()

		# a,b,c are coefficients in above quadratic
		a = B.length_squared()
		b = B.dot(shifted) # the two cancels; discriminant and t are adjusted accordingly
		c = shifted.length_squared() - self.radius * self.radius
		discriminant = b*b - a*c

		if discriminant < 0:
			return False

		t = (-b - math.sqrt(discriminant)) / a
		if t <= t_min or t >= t_max:
			return False

		self.t = t
		self.p = r.point_at_parameter(t)
		self.normal = (self.p - self.center) / self.radius
		return True

