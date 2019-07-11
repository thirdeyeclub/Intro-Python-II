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

    'narrow':   Room("Narrow Passage", """The narrow passage continues eastwards but bends here from west
to north. The smell of treasure permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),

	'chamber': Room("Large Chamber", """You stand in the center of a very large chamber. There is a wooden door to th east. To the south you hear chattering. To your north you see an inviting tunnel."""),

	'storeroom' : Room("Storage Room", """A small storage room."""),

	'trap_tunnel' : Room("Trap Tunnel", "You are in a room full of bear traps, you the only exit is south , where you came from. Be careful now."),

	'dark_passage' : Room("Pitch Black Passageway","""You can see nothing. You feel the walls to try to make sense of your surrondings,the walls of the cave are cold as ice, the hair on the back of your neck stands up. You can't tell how big the room is."""),

	'snake_room': Room("Snake Nest","""A Snake appears and does something"""),

	'deadend' : Room("Dead End", """You have reached a dead end, best go back"""),

	'gold_room' : Room("Gold Room", """Finally some real treasure! But oh no! The way you came from seems to have been sealed off. You should look for another exit."""),

	'crawl_space' : Room("Crawl Space","""You are squezzed tightly in a small cave tunnel. The only directions you can go are more south or towards the west, how you can still tell the directions underground noone knows."""),

	'spike_pit': Room("Pit","""You have fallen into a pit full of spikes. You have died"""),

	'dungeon': Room("Dungeon","""You are in a dungeon but you are not alone."""),
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
room['narrow'].e_to = room['chamber']
room['chamber'].w_to = room['narrow']
room['chamber'].e_to = room['storeroom'] #where you find axe to fight the snake
room['chamber'].n_to = room['trap_tunnel']
room['chamber'].s_to = room['dark_passage']
room['storeroom'].w_to = room['chamber']
room['trap_tunnel'].s_to = room['chamber']
room['dark_passage'].n_to = room['chamber']
room['dark_passage'].e_to = room['snake_room'] #snake fight
room['snake_room'].w_to = room['dark_passage']
room['dark_passage'].s_to = room['deadend']
room['deadend'].n_to = room['dark_passage']
room['dark_passage'].w_to = room['gold_room'] #you find a lot of gold but there is no way back
room['gold_room'].s_to = room['crawl_space']
room['crawl_space'].n_to = room['gold_room'] 
room['crawl_space'].s_to = room['spike_pit'] #you die
room['crawl_space'].w_to = room['dungeon'] #fight?



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
compass_direction = ["e" ,"n", "s" , "w"]

print("     You stand on the outskirts of town\n     To look around type d")
while True:
	cmd = input('     >')
	# moving
	current_room = player.current_room
	if cmd in compass_direction:
		player.travel(cmd)

	elif cmd == 'q':
		break
	elif cmd == 'd':
		print(f"    {player.current_room.name}\n    {player.current_room.description} \n    Around you there is {player.current_room.items}")
	elif cmd == 'i':
		print(f"You the have following items {str(player.items)}")
	else:
		print('Valid choices are n, e, s, w for moving in a direction, \td for displaying items in the room. \t i for displaying what you are carrying \t get (item) or drop (item) to access items in the room \t or q to end the game\n') 

