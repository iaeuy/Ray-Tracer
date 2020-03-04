class Material():
	def scatter(self, r_in, p, n):
		"""
		Given ray intersecting material at
		vector p with normal vector n, give 
		scattered ray and attenuation.
		Attenuation is a Vec3 which is multiplied
		entrywise with output.
		If ray is absorbed, return None, None.
		"""
		raise NotImplementedError()