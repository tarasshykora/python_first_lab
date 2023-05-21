from models.dishwasher import Dishwasher


class ConsumerDishwasher(Dishwasher):
	def get_power_consumption_per_cycle(self):
		return 1000

	def __init__(self, max_capacity, current_capacity):
		super().__init__()
		self.max_capacity = max_capacity
		self.current_capacity = current_capacity
