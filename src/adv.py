from room import Room
from player import Player

# Declare all the rooms

room = {
    'outside':
    Room(
        "Outside Cave Entrance",
        "North of you, the cave mount beckons"
    ),

    'foyer':
    Room(
        "Foyer",
        """Dim light filters in from the south. Dusty passages run north and east."""
    ),

    'overlook':
    Room(
        "Grand Overlook",
        """A steep cliff appears before you, falling into the darkness. Ahead to the north, a light flickers in the distance, but there is no way across the chasm."""
    ),

    'narrow':
    Room(
        "Narrow Passage",
        """The narrow passage bends here from west to north. The smell of gold permeates the air."""
    ),

    'treasure':
    Room(
        "Treasure Chamber",
        """You've found the long-lost treasure chamber! Sadly, it has already been completely emptied by earlier adventurers. The only exit is to the south."""
    ),
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
player = Player(
    input(
        'Welcome To My Adventure Game! \nType your player name to begin => '), room['outside']
)

playerName = player.name
location = player.current_room

print(f'Hello Agent {playerName}!, your current location is the {location}')

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

while True:
    playerMove = input(
        'Select the direction you would like to go \n [ n for North ] \t [ w for West ] \n [ s for South ] \t [ e for East ] \n \t Press q to cancel the game \nType Selection => '
    )

    if playerMove == 'n':
        if location.n_to != 0:
            location = location.n_to
            print(f'Your new location is {location}')
        else:
            print(f'Invalid direction, please select a different move')

    elif playerMove == 's':
        if location.s_to != 0:
            location = location.s_to
            print(f'You are now in the {location}')
        else:
            print(f'Invalid direction, please select a different move')

    elif playerMove == 'w':
        if location.w_to != 0:
            location = location.w_to
            print(f'You have switched locations to the {location}')
        else:
            print(f'Invalid direction, please select a different move')

    elif playerMove == 'e':
        if location.e_to != 0:
            location = location.e_to
            print(f'You just moved to the {location}')
        else:
            print(f'Invalid direction, please select a different move')

    elif playerMove == 'q':
        print('----- Goodbye and thanks for playing -----')
        exit()


# NOTES
# GUIDED SOLUTION FROM THE LECTURE

# player = Player(input("What is your name? "), room['outside'])
# print(f"Hello, {player.name}.")
# print(player.current_room)
# while True:
#     cmd = input("-> ").lower()
#     if cmd in ["n", "s", "e", "w"]:
#         # Move to that room
#         player.travel(cmd)
#     elif cmd == "q":
#         print("Goodbye!")
#         exit()
#     else:
#         print("I did not understand that command.")
