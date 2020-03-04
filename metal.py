import random
from material import Material
from vec3 import Vec3
from ray import Ray

class Metal(Material):
	def __init__(self, albedo, fuzz = 0):
		self.albedo = albedo
		self.fuzz = fuzz if abs(fuzz) < 1 else 1

	def scatter(self, r_in, p, n):
		reflected = reflect(r_in.direction().unit_vector(), n)
		reflected += random_in_unit_sphere()*self.fuzz
		if reflected.dot(n) <= 0:
			return None, None
		
		scattered = Ray(p, reflected)
		attenuation = self.albedo
		return scattered, attenuation

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