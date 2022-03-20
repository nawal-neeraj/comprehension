class Celsius:
    def __init__(self, temprature=0) -> None:
        self.set_temprature(temprature)
        # self.temprature = temprature
        
    def to_fahrenheit(self):
        print(self.get_temprature())
        return (self.get_temprature() * 1.8) + 32
    
    def get_temprature(self):
        return self._temprature
    
    def set_temprature(self, value):
        if value < -273.15:
            raise ValueError("Not possible")
        self._temprature = value
        
        
check_value = Celsius(30)

# check_value._temprature = 30 
print(f"===>fahrenheit {check_value.to_fahrenheit()}")
print(f"===>Celcius {check_value.__dict__}")

set_method = check_value.set_temprature(-300)
print(set_method)