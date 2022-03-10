class lists_class:
    def remove_list(self, a):
        name= ["name1", "name2", 3, "name4", 5, "name6"]
        print(f"initial values {name}")
        name.remove(name[a])
        return name
