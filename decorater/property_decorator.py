class Celsius:
    def __init__(self, temprature = 0) -> None:
        self.temprature = temprature
        
        
    def to_fahrenheit(self):
        temp = (self.temprature * 1.8) + 32
        return temp
    
convert = Celsius()

convert.temprature = 20
print(f"===> To Celsius {convert.temprature}")

print(f"===> To fahrenheit {convert.to_fahrenheit()}")

print(f"===> To magic method {convert.__dict__}")