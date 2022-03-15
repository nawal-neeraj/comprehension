class OverLoading:
    def over_loading_example(self, value_one= None, value_two= None, value_three= None):
        if value_one != None and value_two != None and value_three != None:
            c = value_one + value_two + value_three
            print(c)
            return c
        elif value_one != None and value_two != None:
            c = value_one + value_two
            print(c)
            return c
        else:
            print(value_one)
            return value_one
       
s1 = OverLoading()

print("Pass three parameters")
s1.over_loading_example(1,2,3)

print("Pass two parameters")

s1.over_loading_example(1,2)

print("Pass only one parameter")

s1.over_loading_example(2)
