from room import Room

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons",
                     {'n': 'foyer'}),

    'foyer':    Room("Foyer",
                     """Dim light filters in from the south. Dusty
passages run north and east.""",
                     {'n': 'overlook', 'e': 'narrow', 's': 'outside'}),

    'overlook': Room("Grand Overlook",
                     """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""",
                     {'s': 'foyer'}),

    'narrow':   Room("Narrow Passage",
                     """The narrow passage bends here from west
to north. The smell of gold permeates the air.""",
                     {'w': 'foyer', 'n': 'treasure'}),

    'treasure': Room("Treasure Chamber",
                     """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""",
                     {'s': 'narrow'}),
}


# Link rooms together

# room['outside'].n_to = room['foyer']
# room['foyer'].s_to = room['outside']
# room['foyer'].n_to = room['overlook']
# room['foyer'].e_to = room['narrow']
# room['overlook'].s_to = room['foyer']
# room['narrow'].w_to = room['foyer']
# room['narrow'].n_to = room['treasure']
# room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.

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


def monokeys(c):
    print('monokey')


def command_router(command):
    if len(command) == 1:
        monokeys(command)
    else:
        print('multikey')


print("\033[?1049h\033[H")
print("Welcome!")

while True:
    res = input('>')
    if res == 'q':
        print("\033[?1049l")
        break
    else:
        command_router(res)

# look into player's location
# thumb over the exit identities

# Add a REPL parser to `adv.py` that accepts directional commands
# to move the player
# After each move, the REPL should print the name and description of
# the player's current room
# Valid commands are `n`, `s`, `e` and `w` which move the player
# North, South, East or West
# The parser should print an error if
# the player tries to move where there is no room.

  # * Until now, the parser could just understand one sentence form:

  #    `verb`

  #   such as "n" or "q".

  # * But now we want to add the form:

  #   `verb` `object`

  #   such as "take coins" or "drop sword".

# * Add the `inventory`/'i' command that shows a list of items currently
#   carried by the player.
