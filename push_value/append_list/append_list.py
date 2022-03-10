class AppendLlist:
    list_items = ["python", "Js", "ReactJs", "NextJs", "React-Native", "Flutter", "Php", "NodeJs"]
    
    def list_data(self):
        self.new_list = [i for i in self.list_items if "Js" in i ]
        return self.new_list