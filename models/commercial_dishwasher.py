from models.dishwasher import Dishwasher


class CommercialDishwasher(Dishwasher):
	def get_power_consumption_per_cycle(self):
		return 1500

	def __init__(self, glasses_per_hour):
		super().__init__()
		self.glasses_per_hour = glasses_per_hour
