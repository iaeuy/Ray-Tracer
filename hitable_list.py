from hitable import Hitable

class HitableList(Hitable):
	def __init__(self, hitables):
		super().__init__()
		self.hitables = hitables 

	def hit(self, r, t_min, t_max):
		hit = False
		closest = t_max

		for obj in self.hitables:
			if obj.hit(r, t_min, t_max):
				hit = True
				if t_min < obj.t and obj.t < closest:
					closest = obj.t
					self.t = obj.t
					self.p = obj.p
					self.normal = obj.normal
					self.matrl = obj.matrl 

		return hit

