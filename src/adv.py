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
player = Player(name='Tyler', current_room=room['outside'])

# Create items 
sword = Item(name='sword', description='A somewhat rusty blade.')
shield = Item(name='shield', description='An old but sturdy shield.')

# Add items to foyer
foyer_items = [sword, shield]
room['foyer'].add_items(foyer_items)



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


    instructions = """\n INSTRUCTIONS:
    To check your inventory, type: 'check inventory'
    To change items, type: 'take/drop' [item_name]
    To move to another area, choose a single directon: 'N, S, E, W'
    To exit the game, type: 'q'
    \nType Here:    """

    error = "\n>> ERROR, please enter a valid input."
    valid_move = ['n', 's', 'e', 'w']



    print("\n----------")
    # Display player's current room and its description
    player.location()
    # Display any items in current room
    player.current_room.get_room_items()
    # Take user input, clean, and add to list
    user_input = input(instructions).strip().lower().split(' ')

    # Parse for items or movement based on len of user input
    input_length = len(user_input)
    
    # [Verb] Parsing
    if input_length == 1:
        user_input = user_input[0]
        if user_input in valid_move:
            # Player movement and location updating
            try:
                player.move(user_input)
                
            except:
                print(invalid_room)
        # Exit program
        elif user_input[0] == 'q':
            print("Thanks for playing!")
            break
        # Input error handling
        else:
            print(error)

    # [Verb] [Object] Parsing       
    elif input_length == 2:
        action = user_input[0]
        item_names = user_input[1]
        player.item_action(action, item_names)


    else:
        print(error)
