from abc import abstractmethod

class Dishwasher:
    __instance = None

    def __init__(self, model="Bosch series 4", max_capacity=14, current_capacity=7, is_on=False):
        self.model = model
        self.max_capacity = max_capacity
        self.current_capacity = current_capacity
        self.is_enabled = is_on

    @abstractmethod
    def get_power_consumption_per_cycle(self):
        pass

    def load_dishes(self, count):
        if self.current_capacity + count > self.max_capacity:
            self.current_capacity = self.max_capacity
        else:
            self.max_capacity += count

    def clean_dishes(self, count):
        self.count = None

    def turn_on(self):
        return self.is_enabled

    def turn_off(self):
        return False

    def __str__(self):
        return f"Dishwasher: model = {self.model}, max_capacity = {self.max_capacity}," \
               f" current_capacity = {self.current_capacity}, is_on = {self.is_enabled}"



