from vec3 import Vec3

def create_gradient():
	file = open('out/gradient.ppm', 'w')
	
	nx = 200
	ny = 100

	# header
	file.write("P3 \n")
	file.write(str(nx) + " " + str(ny) + "\n")
	file.write("255\n")

	for j in range(ny - 1, -1, -1):
		for i in range(nx):
			v = pixel_color(i, j, nx, ny)
			file.write(str(v))

	file.close()

def pixel_color(i, j, nx, ny): # rgb for pixel at ji
	return Vec3(int(255.99 * i / nx), int(255.99 * j / ny), 100)
	# return int(255.99 * i / nx), int(255.99 * j / ny), 51
	# return int(255.99 * i / nx), int(255.99 * j / ny), int(255.99 * (i+1) / (i+j+1))
	# return int(255.99 * (ny-j) / ny), int(255.99 * (j*j+1) / (i*i+j*j+1)), int(255.99 * (i+1) / (i+j+1))

def main():
	create_gradient()
	

if __name__ == '__main__':
	main()