from models.dishwasher import Dishwasher


class ClinicalDishwasher(Dishwasher):
	def get_power_consumption_per_cycle(self):
		return 2000

	def __init__(self, power, duration_of_one_cycle_of_sterilization, max_temperature_of_sterelization):
		super().__init__()
		self.power = power
		self.duration_of_one_cycle_of_sterilization = duration_of_one_cycle_of_sterilization
		self.max_temperature_of_sterilization = max_temperature_of_sterelization

