import abc

class Animal():
    
    @abc.abstractmethod
    def get_name(self):
        raise NotImplemented()
    
    @abc.abstractmethod
    def get_weight(self):
        raise NotImplemented()
    
    @abc.abstractmethod
    def is_horn_present(self):
        raise NotImplemented

class Cat(Animal):
    
    def __init__(self) -> None:
        super().__init__()
        self._name = "cat"
        self._weight = "12kg"
        self._horn = False
    
    def get_name(self):
        return self._name
    
    def get_weight(self):
        return self._weight
    
    def is_horn_present(self):
        return self._horn
    
class Cow(Animal):
    
    def __init__(self) -> None:
        super().__init__()
        self._name = "Cow"
        self._weight = "120kg"
        self._horn = True
    
    def get_name(self):
        return self._name
    
    def get_weight(self):
        return self._weight
    
    def is_horn_present(self):
        return self._horn


cat = Cat()
print(cat.get_name())

cow = Cow()
print(cow.get_name())
