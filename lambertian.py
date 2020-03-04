import random
from material import Material
from vec3 import Vec3
from ray import Ray

class Lambertian(Material):
	def __init__(self, albedo):
		self.albedo = albedo

	def scatter(self, r_in, p, n):
		target = p + n + random_in_unit_sphere()
		scattered = Ray(p, n + random_in_unit_sphere())
		attenuation = self.albedo
		return scattered, attenuation

def random_in_unit_sphere():
	"""
	Return random Vec3 in unit sphere.
	Samples from cube until it lies in sphere.
	"""
	while True:
		p = Vec3(random.random(), random.random(), random.random()) * 2 - Vec3(1, 1, 1)
		if p.length_squared() < 1:
			return p