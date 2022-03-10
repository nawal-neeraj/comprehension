def method_one(*args, **kwargs):
    print(f"===>args: {args}, ===>Kwargs: {kwargs}")


method_one(1,"two", myarg1="myarg_value1", myarg2="myarg_value2")