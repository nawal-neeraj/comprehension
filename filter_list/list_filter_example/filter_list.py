class FilterClass:
    
    def filter_list_value(self ,a):
    # def filter_list_value(a):
        list_values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        print(f"all values {list_values} and the range of list is {len(list_values)}")

        new_list = [i for i in list_values if i % a == 0]

        return new_list
