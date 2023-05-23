from models.clinical_dishwasher import ClinicalDishwasher
from models.commercial_dishwasher import CommercialDishwasher
from models.glassware_washer import GlasswareWasher


class DishwasherManager:
    """
    DishwasherManager class

    This class has methods for finding the highest dishwasher and the one that consumes the most energy.

    Attributes:
    List of dishwashers

    Methods:
    add_dishwashers: Adds a dishwasher to the collection
    find_electricity_consumption_greater_than: Finds the dishwasher that consumes the most energy
    find_max_capacity_higher_than: Finds the highest dishwashers
    """

    def __init__(self):
        self.dishwasher_list = []

    def add_dishwasher(self, dishwasher):
        """

        Adds a dishwasher to the collection

        """

        self.dishwasher_list.append(dishwasher)

    def find_electricity_consumption_greater_than(self, power):
        """
        Finds the dishwasher that consumes the most energy

        Args:
            power: Method searching for power

        Returns:
            list: A list of dishwasher that have greater electricity consumption than indicated

        """
        return list(filter(lambda dishwasher: dishwasher.get_power_consumption_per_cycle() > power, self.dishwasher_list))

    def find_max_capacity_higher_than(self, capacity):
        """
         Finds dishwashers with max capacity

         Args:
         capacity: Method searching for capacity

        Returns:
        list: A list of dishwashers that have indicated max capacity
        :
        """
        return list(filter(lambda dishwasher: dishwasher.get_max_capacity() > capacity, self.dishwasher_list))




if __name__ == "__main__":
    dishwasher_manager = DishwasherManager()
    dishwasher_manager.add_dishwasher(ClinicalDishwasher("Maidaid MH525", 14, 7, True, 1.74, 18, 100, 1, 15, 35))
    dishwasher_manager.add_dishwasher(GlasswareWasher("Glory-2 / F2", 12, 3, False, 2, 100, True, 120))
    dishwasher_manager.add_dishwasher(CommercialDishwasher("Jackson DishStar HT-E", 20, 13, True, 2.5, 200, 970))

    my_list = (range(20))
    result = list(filter(lambda num : (num % 2), my_list))
    print(result)

    print("All dishwashers:")
    for dishwasher in dishwasher_manager.dishwasher_list:
        print(dishwasher)

    print("\nDishwasher which have greater electricity consumption than indicated:")
    electro_dishwashers = dishwasher_manager.find_electricity_consumption_greater_than(1)
    for dishwasher in electro_dishwashers:
        print(dishwasher)

    print("\nDishwashers that have greater max capacity than indicated:")
    max_dishwashers = dishwasher_manager.find_max_capacity_higher_than(14)
    for dishwasher in max_dishwashers:
        print(dishwasher)
