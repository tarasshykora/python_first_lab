from models.dishwasher import Dishwasher


class CommercialDishwasher(Dishwasher):
    """
    CommercialDishwasher class

    Args:
        model
        max_capacity
        current_capacity
        is_enabled
        electricity_consumption_per_cycle
        count
        glasses_per_hour

    Methods:
        get_power_consumption_per_cycle: abstract method implemented by child classes

        Returns:
        power consumption per cycle

    """

    def get_power_consumption_per_cycle(self):
        """
        Gets information about power consumption per cycle

        Returns:
            power consumption per cycle of dishwasher
        """
        return 2000

    def __init__(self, model, max_capacity, current_capacity, is_enabled,
                 electricity_consumption_per_cycle, count, glasses_per_hour):
        super().__init__(model, max_capacity, current_capacity, is_enabled,
                         electricity_consumption_per_cycle, count)
        self.glasses_per_hour = glasses_per_hour

    def __str__(self):
        return f"model={self.model}, max_capacity={self.max_capacity}," \
               f" current_capacity={self.current_capacity}," \
               f"is_enabled={self.is_enabled}," \
               f" electricity_consumption_per_cycle={self.electricity_consumption_per_cycle}," \
               f"count={self.count}, glasses_per_hour={self.glasses_per_hour}"


