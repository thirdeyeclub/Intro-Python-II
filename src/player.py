# Write a class to hold player information, e.g. what room they are in
# currently.
from item import Item

# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    def __init__(self, name, starting_room):
        self.name = name
        self.current_room = starting_room
        self.items = []
        self.ego = 4
    def travel(self, direction):
        # Check if there's a valid room in the direction
        if getattr(self.current_room, f"{direction}_to") is not None:
            # If so, update current_room to new room and print description
            self.current_room = getattr(self.current_room, f"{direction}_to")
            print(self.current_room)
        else:
            # Else print an error message
            print("Sorry! there's no room here.", "\n")

    # def get_item(self, Item):
    #     self.items.append(Item)

	# def drop_item(self, item):
	# 	if Item in self.items:
	# 		self.items.remove(item)
	# 	else:
	# 		print(f"You are not carrying an item")
    