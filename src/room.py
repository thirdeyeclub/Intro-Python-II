class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.items = ["nothing of intrest"] #items
        self.to_n = None
        self.to_e = None
        self.to_s = None
        self.to_w = None
    def __str__(self):
        str = f"""\n {self.name} \n {self.description}\n {self.items}"""
        return str