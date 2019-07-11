class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.items = [] #items
        self.to_n = None
        self.to_e = None
        self.to_s = None
        self.to_w = None
    def __str__(self):
        str = f"""
                \n {self.name} 
                \n {self.description}
                \n {self.items}"""
        return str
    
    # def move_to(self, direction):
	# 	if direction == "n":
	# 		return self.n_to
	# 	elif direction == "e":
	# 		return self.e_to
	# 	elif direction == "s":
	# 		return self.s_to
	# 	elif direction == "w":
	# 		return self.w_to

	# 	else:
    #             return None
    
    




# Implement a class to hold room information. This should have name and
# description attributes.