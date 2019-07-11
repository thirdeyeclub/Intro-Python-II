from room import Room
from player import Player
from item import Item
from items import items
# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                    "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
player = Player("Name", room["outside"])

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
compass_direction = ["e" ,"n" "s" , "w"]

while True:
	cmd = input('--->  ')
	# moving
	_current_room = player._current_room
	if cmd in compass_direction:
		direction = cmd
		if getattr(player._current_room, f"{direction}_to") == None:
			print("you cannot go that way!")
		else:
			player._current_room = getattr(player._current_room, f"{direction}_to")
			print(player._current_room)
	elif cmd == 'q':
		print("Exiting Game")
		break
	elif cmd == 'd':
		print(f"{player._current_room.name} has the following items {player._current_room.items}")
	elif cmd == 'i':
		print(f"You the following items {player.items}")
	else:
		print('Valid choices are n, e, s, w for moving in a direction, \td for displaying items in the room. \t i for displaying what you are carrying \t get (item) or drop (item) to access items in the room \t or q to end the game\n') 

