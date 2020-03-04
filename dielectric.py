import math
import random
from material import Material
from vec3 import Vec3
from ray import Ray

class Dielectric(Material):
	def __init__(self, refrac_index):
		self.refrac_index = refrac_index

	def scatter(self, r_in, p, n):
		v = r_in.direction()
		if v.dot(n) > 0:
			outward_normal = -n
			refrac_ratio = self.refrac_index
		else:
			outward_normal = n
			refrac_ratio = 1 / self.refrac_index

		v_refrac  = refract(v, outward_normal, refrac_ratio)
		if v_refrac:
			return Ray(p, v_refrac), Vec3(1, 1, 1)
		else:
			return Ray(p, reflect(v, n)), Vec3(1, 1, 1)
			# return None, None


def refract(v, n, refrac_ratio):
	"""
	v: incoming vector
	n: normal vector
	refrac_ratio: n1/n2, ratio of refractive indices

	Computes v_refrac according to snells law. Return None if
	refraction is not possible (i.e .total internal reflection)
	"""
	uv = v.unit_vector()
	c = -uv.dot(n)

	discriminant = 1 - refrac_ratio * refrac_ratio * ( 1 - c * c)
	if discriminant <= 0:
		return None

	return uv * refrac_ratio + n * (refrac_ratio * c - math.sqrt(discriminant))
	# uv = v.unit_vector()
	# dt = uv.dot(n)
	# discriminant = 1.0 - refrac_ratio * refrac_ratio * (1 - dt * dt)
	# if discriminant > 0:
	# 	return (uv - n * dt) * refrac_ratio - n * math.sqrt(discriminant)
	# else:
	# 	return None


def reflect(v, n):
	# gives reflection of v hitting surface with normal n
	return v - n * 2 * v.dot(n)

def random_in_unit_sphere():
	"""
	Return random Vec3 in unit sphere.
	Samples from cube until it lies in sphere.
	"""
	while True:
		p = Vec3(random.random(), random.random(), random.random()) * 2 - Vec3(1, 1, 1)
		if p.length_squared() < 1:
			return p	
