import sys
import math
import random
from vec3 import Vec3
from ray import Ray
from camera import Camera
from hitable_list import HitableList
from sphere import Sphere
from lambertian import Lambertian
from metal import Metal
from dielectric import Dielectric

def create_image(name):
	file = open("out/" + name + ".ppm", "w")
	
	nx = 200
	ny = 100

	# ppm header
	file.write("P3 \n") # rgb setting
	file.write(str(nx) + " " + str(ny) + "\n")
	file.write("255\n")

	for j in range(ny - 1, -1, -1):
		for i in range(nx):
			v = three_spheres(i, j, nx, ny) # CHANGE THIS; rgb for pixel at ji
			v = Vec3(math.sqrt(v.x()), math.sqrt(v.y()), math.sqrt(v.z())) * 16 # gamma correction
			v = Vec3(int(v.x()), int(v.y()), int(v.z())) # round down to integers
			file.write(str(v))

	file.close()

def gradient(i, j, nx, ny): # rgb for pixel at ji
	return Vec3(int(255.99 * i / nx), int(255.99 * j / ny), 150)

def origin_to_pixel(i, j, nx, ny):
	"""
	Returns the ray from the origin to given pixel,
	where the image is a rectangle with upper left 
	corner (-2, 1, -1) and lower right corner (2, -1, -1)
	"""
	return Camera().get_ray(i / nx, j / ny)
	# return Ray(origin, lower_left_corner + horizontal * i / nx + vertical * j / ny)

def blue_to_white(i, j, nx, ny):
	r = origin_to_pixel(i, j, nx, ny)
	v = r.direction().unit_vector() # use y-coordinate of unit direction to scale blueness
	t = (v.y() + 1) / 2 # ranges between 0 and 1
	return Vec3(255.99, 255.99, 255.99) * (1 - t)  + Vec3(255.99 * 0.5, 255.99 * 0.7, 255.99) * t

def naive_sphere(i, j, nx, ny):
	s = Sphere(Vec3(0,0,-1), 0.5)
	r = origin_to_pixel(i, j, nx, ny)
	if s.hit(r, 0, float("inf")):
		# return Vec3(255, 0, 0)
		k = (abs(s.normal.dot(r.direction().unit_vector())) + 1) / 2
		return Vec3(200, 100, 30) * k
	else:
		return blue_to_white(i, j, nx, ny)

def colored_sphere(i, j, nx, ny):
	s = Sphere(Vec3(0,0,-1), 0.5)
	r = origin_to_pixel(i, j, nx, ny)
	if s.hit(r, 0, float("inf")):
		return (s.normal + Vec3(1, 1, 1)) * 255.99 / 2
	else:
		return blue_to_white(i, j, nx, ny)

def two_spheres(i, j, nx, ny):
	s1 = Sphere(Vec3(0,0,-1), 0.5)
	s2 = Sphere(Vec3(0, -100.5, -1), 100)
	spheres = HitableList([s1, s2])

	if spheres.hit(origin_to_pixel(i, j, nx, ny), 0, float("inf")):
		return (spheres.normal + Vec3(1, 1, 1)) * 255.99 / 2
	else:
		return blue_to_white(i, j, nx, ny)

def two_spheres_aa(i, j, nx, ny, num_samples = 100):
	s1 = Sphere(Vec3(0,0,-1), 0.5)
	s2 = Sphere(Vec3(0, -100.5, -1), 100)
	spheres = HitableList([s1, s2])
	cam = Camera()

	color = Vec3(0, 0, 0)
	for k in range(num_samples):
		u = (i + random.random())/ nx
		v = (j + random.random())/ ny
		r = cam.get_ray(u, v)
		if spheres.hit(r, 0, float("inf")):
			color += (spheres.normal + Vec3(1, 1, 1)) * 255.99 / 2
		else:
			v = r.direction().unit_vector() # use y-coordinate of unit direction to scale blueness
			t = (v.y() + 1) / 2 # ranges between 0 and 1
			color += Vec3(255.99, 255.99, 255.99) * (1 - t)  + Vec3(255.99 * 0.5, 255.99 * 0.7, 255.99) * t
	return color / num_samples

def diffuse_sphere(i, j, nx, ny, num_samples = 100):
	s1 = Sphere(Vec3(-0.75, 0.75, -1), 0.5, Lambertian(Vec3(0.8, 0.3, 0.3)))
	s2 = Sphere(Vec3(0, -100.5, -1), 100, Lambertian(Vec3(0.2, 0.6, 0.2)))
	spheres = HitableList([s1, s2])
	cam = Camera()

	def color(r, world):
		if world.hit(r, 0.001, float("inf")):
			scattered, attenuation = world.matrl.scatter(r, world.p, world.normal)
			if scattered:
				return color(scattered, world) * attenuation
			else:
				return Vec3(0, 0, 0)
		else:
			v = r.direction().unit_vector() # use y-coordinate of unit direction to scale blueness
			t = (v.y() + 1) / 2 # ranges between 0 and 1
			return Vec3(255.99, 255.99, 255.99) * (1 - t)  + Vec3(255.99 * 0.5, 255.99 * 0.7, 255.99) * t

	col = Vec3(0,0,0)
	for k in range(num_samples):
		col += color(cam.get_ray( (i + random.random()) / nx, (j + random.random()) / ny), spheres)

	return col / num_samples

def three_spheres(i, j, nx, ny, num_samples = 100):
	s1 = Sphere(Vec3(0, 0, -1), 0.5, Lambertian(Vec3(0.1, 0.2, 0.5)))
	s2 = Sphere(Vec3(0, -100.5, -1), 100, Lambertian(Vec3(0.8, 0.8, 0.0)))
	s3 = Sphere(Vec3(-1,0,-1), 0.5, Dielectric(2.5))
	s4 = Sphere(Vec3(1,0,-1), 0.5, Metal(Vec3(0.8, 0.6, 0.2), 0.0))
	spheres = HitableList([s1, s2, s3, s4])
	cam = Camera()
	# cam = Camera(origin = Vec3(0, 0, 0), 
	# 			lower_left_corner = Vec3(-3, -1.5, -1), 
	# 			horizontal = Vec3(6, 0, 0), 
	# 			vertical = Vec3(0, 3, 0))

	def color(r, world, depth):
		if world.hit(r, 0.001, float("inf")):
			scattered, attenuation = world.matrl.scatter(r, world.p, world.normal)
			if not scattered or depth >= 50:
				return Vec3(0, 0, 0)
			return color(scattered, world, depth + 1) * attenuation
		else:
			v = r.direction().unit_vector() # use y-coordinate of unit direction to scale blueness
			t = (v.y() + 1) / 2 # ranges between 0 and 1
			return Vec3(255.99, 255.99, 255.99) * (1 - t)  + Vec3(255.99 * 0.5, 255.99 * 0.7, 255.99) * t

	col = Vec3(0,0,0)
	for k in range(num_samples):
		col += color(cam.get_ray( (i + random.random()) / nx, (j + random.random()) / ny), spheres, 0)

	return col / num_samples


def main():
	create_image(sys.argv[1])

if __name__ == '__main__':
	main()