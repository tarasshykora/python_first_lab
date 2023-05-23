"""
Importing abstract base class
"""
from abc import ABC, abstractmethod


class Dishwasher(ABC):
    """
    Dishwasher abstract class

    Attributes:
        model
        max_capacity
        current_capacity
        is_on
        electricity_consumption_per_cycle
        count

    Methods:
        get_power_consumption_per_cycle: abstract method
        clean_dishes
        load_dishes
        turn_off
        turn_on
    """

    #pylint: disable=too-many-arguments
    def __init__(self, model=None, max_capacity=0, current_capacity=0,
                 is_on=False, electricity_consumption_per_cycle=0,
                 count=0):
        self.model = model
        self.max_capacity = max_capacity
        self.current_capacity = current_capacity
        self.is_enabled = is_on
        self.electricity_consumption_per_cycle = electricity_consumption_per_cycle
        self.count = count

    @abstractmethod
    def get_power_consumption_per_cycle(self):

        """

        get_power_consumption_per_cycle: abstract method which defines power consumption per cycle

        """


    def clean_dishes(self):
        """

        clean_dishes: method which removes dishes from dishwasher

        """
        self.current_capacity = None

    def load_dishes(self):
        """

        load_dishes: method which loads dishes to dishwasher

        """
        if self.current_capacity + self.count > self.max_capacity:
            self.current_capacity = self.max_capacity
        else:
            self.max_capacity += self.count

    def turn_on(self):
        """

        turn_on: method which turns on dishwasher

        """
        self.is_enabled = True

    def turn_off(self):
        """

        turn_off: method which turns of dishwasher

        """
        self.is_enabled = False

    def get_max_capacity(self):
        """

        get_max_capacity: Gets max capacity of dishwasher

        Returns:
            max capacity
        """
        return self.max_capacity

    def __str__(self):
        return f"model={self.model}, max_capacity={self.max_capacity}," \
               f" current_capacity={self.current_capacity}," \
               f"is_enabled={self.is_enabled}," \
               f" electricity_consumption_per_cycle={self.electricity_consumption_per_cycle}," \
               f"count={self.count}"
