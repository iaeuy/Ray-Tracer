class Hitable:
	def __init__(self):
		self.t = None # for intersection point of ray
		self.p = None # intersection vector
		self.normal = None # unit normal vector
		self.matrl = None # material

	def hit(self, r, t_min, t_max):
		"""
		Abstract method. Returns True if ray r hits
		with t_min < t < t_max. If True, modify t, p, normal
		in place.
		"""
		raise NotImplementedError()
