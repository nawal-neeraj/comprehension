class Celsius:
    def __init__(self, temperature=0):
        self.temperature = temperature

    def to_fahrenheit(self):
        return (self.temperature * 1.8) + 32

    def get_temperature(self):
        return self._temperature

    def set_temperature(self, value):
        if value < -273.15:
            raise ValueError("Not possible")
        self._temperature = value

    temperature = property(get_temperature, set_temperature)
    
    
check_value = Celsius(23)

print(f"===>fahrenheit {check_value.to_fahrenheit()}")

check_value.temperature= -300
print(f"===>Using property {check_value.to_fahrenheit()}")