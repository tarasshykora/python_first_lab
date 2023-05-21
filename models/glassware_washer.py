from models.dishwasher import Dishwasher


class GlasswareWasher(Dishwasher):
	def get_power_consumption_per_cycle(self):
		return 2000

	def __init__(self, has_itl_automatic_door, weight):
		super().__init__()
		self.has_itl_automatic_door = has_itl_automatic_door
		self.weight = weight

