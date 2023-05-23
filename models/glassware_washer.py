from models.dishwasher import Dishwasher


class GlasswareWasher(Dishwasher):
    """
    GlasswareWasher clas

    Attributes:
        model
        max_capacity
        current_capacity
        is_enabled
        electricity_consumption_per_cycle
        count
        has_itl_automatic_door
        weight
    """

    def get_power_consumption_per_cycle(self):
        """
        Gets information about power consumption per cycle

        Returns:
            power consumption per cycle of dishwasher
        """

        return 2000

    def __init__(self, model, max_capacity, current_capacity, is_enabled,
                 electricity_consumption_per_cycle, count, has_itl_automatic_door, weight):
        super().__init__(model, max_capacity, current_capacity, is_enabled,
                         electricity_consumption_per_cycle, count)
        self.has_itl_automatic_door = has_itl_automatic_door
        self.weight = weight

    def __str__(self):
        return f"model={self.model}, max_capacity={self.max_capacity}," \
               f" current_capacity={self.current_capacity}," \
               f"is_enabled={self.is_enabled}," \
               f" electricity_consumption_per_cycle={self.electricity_consumption_per_cycle}," \
               f"count={self.count}, " \
               f"has_itl_automatic_door={self.has_itl_automatic_door}," \
               f" weight={self.weight}"