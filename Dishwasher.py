class Dishwasher:
    instance = None

    def __init__(self, model="Bosch", max_capacity=4, current_capacity=17, is_on=False):
        self.model = model
        self.max_capacity = max_capacity
        self.current_capacity = current_capacity
        self.is_on = is_on

    def load_dishes(self, count):
        if self.current_capacity + count > self.max_capacity:
            pass
        else:
            self.max_capacity += count

    def clean_dishes(self):
        count = None

    def turn_on(self):
        return True

    def turn_off(self):
        return False

    @staticmethod
    def get_instance():
        if Dishwasher.instance is None:
            Dishwasher.instance = Dishwasher()
        return Dishwasher.instance

    def __str__(self):
        return f"Dishwasher(model={self.model}, max_capacity={self.max_capacity}, current_capacity={self.current_capacity}, is_on={self.is_on})"


dishwasher = [Dishwasher(), Dishwasher("Bosch series 4", 14, 7, True), Dishwasher.get_instance(), Dishwasher.get_instance()]
for dishwashers in dishwasher:
    print(dishwasher)
