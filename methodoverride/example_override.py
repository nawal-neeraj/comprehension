class ExampleOverride:
    
    def __init__(self):
        self.classAvar = "When init is not overridden"
        print(self.classAvar)

class ExampleOver(ExampleOverride):
    def __init__(self):
        self.classAvar = "When init is overridden"
        print(self.classAvar)


check = ExampleOver()
