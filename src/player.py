# Write a class to hold player information, e.g. what room they are in
# currently.
from item import Item

class Player:
    def __init__(self, _current_room):
        self._current_room = _current_room
        self.items = []
        self.ego = 4

    def move_rooms(self, direction):
        if self._current_room.move_rooms(direction) != 'error':
            self._current_room = self._current_room.move_rooms(direction)
            return f'Moved to room {self._current_room.name}'
        else:
            return 'There is no room that way'

    def get_item(self, Item):
        self.items.append(Item)

	def drop_item(self, Item):
		if Item in self.items:
			self.items.remove.Item)
		else:
			print(f"You are not carrying an item")
