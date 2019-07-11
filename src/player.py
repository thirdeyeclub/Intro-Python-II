# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
    def __init__(self, current_room):
        self.current_room = current_room
        self.items = []
        self.ego = 4

    def move_rooms(self, direction):
        if self.current_room.move_rooms(direction) != 'error':
            self.current_room = self.current_room.move_rooms(direction)
            return f'Moved to room {self.current_room.name}'
        else:
            return 'There is no room that way'

    def get_item(self, item):
        self.items.append(item)

    def drop_item(self, item):
        self.items.remove(item)

	def drop_item(self, item):
		if item in self.items:
			self.items.remove(item)
		else:
			print(f"You are not carrying an item")
