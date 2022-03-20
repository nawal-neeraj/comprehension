class Celsius:
    def __init__(self, xyz=0):
        print("initial value")
        self.temperature = xyz

    def to_fahrenheit(self):
        return (self.temperature * 1.8) + 32

    @property
    def temperature(self):
        print("Getting value...")
        return self._temperature

    @temperature.setter
    def temperature(self, value):
        print("Setting value...")
        if value < -273.15:
            raise ValueError("Temperature below -273 is not possible")
        self._temperature = value


# create an object
check_value = Celsius(37)
print("-------")
check_value.temperature = 20
print(check_value.temperature)

# check_value_two = Celsius(32)

# print(check_value.to_fahrenheit())

# coldest_thing = Celsius(-300)