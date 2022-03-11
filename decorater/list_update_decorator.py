from tabnanny import check


class ListUpdate:
    def __init__(self, list_value=[0,3,2]) -> None:
        print(list_value,"init")
        self.list_value = list_value
        
    @property
    def list_value(self):
        return self._list_value
    
    @list_value.setter
    def list_value(self, value):
        print("setter")
        self._list_value = value
        
    # def __getitem__(self, added_value):
    #     print("__getitem__")
    #     return self._list_value[added_value]
    
    def __setitem__(self, added_value, value):
        print("__setitem__")
        self._list_value[added_value] = value
        
check_value = ListUpdate()

check_value[2] = 1

print(check_value.list_value)