#  Create a Car class that has the following characteristics:
#
#      o  It has a gas_level attribute.
#      o  It has a constructor (__init__ method) that takes a float
#         representing the initial gas level and sets the gas level of the car
#         to this value.
#      o  It has an add_gas method that takes a single float value and adds
#         this amount to the current value of the gas_level attribute.
#      o  It has a fill_up method that sets the car’s gas level up to 13.0 by
#         adding the amount of gas necessary to reach this level. It will
#         return a float of the amount of gas that had to be added to the car
#         to get the gas level up to 13.0. However, if the car’s gas level was
#         greater than or equal to 13.0 to begin with, then it doesn’t need to
#         add anything and it simply returns a 0.
#
#  (Note: you can call the add_gas method from within the fill_up method by
#  using this syntax: self.add_gas(amount).)
#
#  Here’s an example.
#
#      example_car = Car(9)
#      print(example_car.fill_up())  # should print 4
#
#      another_car = Car(18)
#      print(another_car.fill_up()) # should print 0


class Car:

    def __init__(self, gas_level):
        """ Create a new car with the given gas_level """
        self.gas_level = gas_level

    def add_gas(self, gas_amount):
        """ Add <gas_amount> gas to the car (assume infinite tank) """
        self.gas_level += gas_amount

    def fill_up(self):
        """
        Add gas to the car (to a maximum of 13.0 units) and return the
        amount added
        """
        gas_added = 0
        if self.gas_level < 13.0:
            gas_added = 13.0 - self.gas_level
            self.add_gas(gas_added)
        return gas_added


def my_test_equal(a, b):
    """ Home-rolled version of testEqual(a, b) """

    if a == b:
        print("Pass")
    else:
        print("Fail")


def main():
    """ Cursory test of Car class """

    my_test_equal(Car(10).fill_up(), 3)
    my_test_equal(Car(20).fill_up(), 0)
    my_test_equal(Car(5.5).fill_up(), 7.5)
    my_test_equal(Car(12.5).fill_up(), 0.5)
    my_test_equal(Car(13).fill_up(), 0)


if __name__ == "__main__":
    main()
