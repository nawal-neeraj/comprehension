from unittest import result
from list_filter_example.filter_list import FilterClass

a:int = 2

# filter = FilterClass.filter_list_value(a)
filter = FilterClass()
result = filter.filter_list_value(a)

print(f"filterd values of List {result} and length of filterd list {len(result)}")