from models.dishwasher import Dishwasher


class ClinicalDishwasher(Dishwasher):
    """
    ClinicalDishwasher class

    Attributes:
        model
        max_capacity
        current_capacity
        is_enabled
        electricity_consumption_per_cycle
        count
        capacity
        power
        duration_of_one_cycle_of_sterilization
        max_temperature_of_sterilization
    """

    def get_power_consumption_per_cycle(self):
        """
        Gets information about power consumption per cycle

        Returns:
            power consumption per cycle of dishwasher
        """
        return 3000

    def __init__(self, model, max_capacity, current_capacity,
                 is_enabled, electricity_consumption_per_cycle,
                 count, capacity, power, duration_of_one_cycle_of_sterilization,
                 max_temperature_of_sterilization):
        super().__init__(model, max_capacity, current_capacity,
                         is_enabled, electricity_consumption_per_cycle, count)
        self.capacity = capacity
        self.power = power
        self.duration_of_one_cycle_of_sterilization = duration_of_one_cycle_of_sterilization
        self.max_temperature_of_sterilization = max_temperature_of_sterilization

    def __str__(self):
        return f"model={self.model}, max_capacity={self.max_capacity}," \
               f" current_capacity={self.current_capacity}," \
               f"is_enabled={self.is_enabled}," \
               f" electricity_consumption_per_cycle={self.electricity_consumption_per_cycle}," \
               f"count={self.count}," \
               f" capacity={self.capacity}, power={self.power}," \
               f"duration_of_one_cycle_of_sterilization={self.duration_of_one_cycle_of_sterilization}," \
               f"max_temperature_of_sterilization={self.max_temperature_of_sterilization}"
