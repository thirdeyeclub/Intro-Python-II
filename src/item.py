class Item:
    def __int__(self, name, description):
        self.name = name
        self.description = description  

class Knife(Item):
    def __int__(self, name, description):
        super().__init__(name, description)
    def use(self):
        return print("You use the knife to free yourself")
