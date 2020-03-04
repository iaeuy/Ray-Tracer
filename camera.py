from ray import Ray
from vec3 import Vec3

class Camera:
	def __init__(self, origin = Vec3(0, 0, 0), 
						lower_left_corner = Vec3(-2, -1, -1), 
						horizontal = Vec3(4, 0, 0), 
						vertical = Vec3(0, 2, 0)):
		self.origin = origin
		self.lower_left_corner = lower_left_corner # vectors for screen
		self.horizontal = horizontal
		self.vertical = vertical

	def get_ray(self, u, v):
		return Ray(self.origin, self.lower_left_corner + 
					 			self.horizontal*u + 
					 			self.vertical*v - 
					 			self.origin)