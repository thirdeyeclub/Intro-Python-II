from room import Room
from player import Player
from item import Item
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

print("      Welcome to the game.\n      You can move with n, e, s, w.     \n      To view your inventory press i")
print("      You stand out side of a cave.\n      Type d to look around")
while True:
	cmd = input('--->  ')
	loot = print("nothing of intrest in this room.")
	# moving
	current_room = player.current_room
	if cmd in compass_direction:
		player.travel(cmd)
	# else: print("you cannot go that way!")

	elif cmd == 'q':
		break
	elif cmd == 'd':
		print(f"    {player.current_room.name}\n    {player.current_room.description} \n    Around you there is {player.current_room.items}")
	elif cmd == 'i':
		print(f"You the following items {str(player.items)}")
	else:
		print('Valid choices are n, e, s, w for moving in a direction, \td for displaying items in the room. \t i for displaying what you are carrying \t get (item) or drop (item) to access items in the room \t or q to end the game\n') 

