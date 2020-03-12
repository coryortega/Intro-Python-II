from room import Room
from player import Player
from item import Item
import colorama
colorama.init()
start = "\033[1;31m"
end = "\033[0;0m"

# Declare all the rooms

room = {
    'outside': Room("Outside Cave Entrance", "North of you, the cave mount beckons", [Item("Bread", "Pretty stale, but it's better than nothing.")]),

    'foyer': Room("Foyer", """Dim light filters in from the south. Dusty passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling into the darkness. Ahead to the north, a light flickers in the distance, but there is no way across the chasm."""),

    'narrow': Room("Narrow Passage", """The narrow passage bends here from west to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure chamber! Sadly, it has already been completely emptied by earlier adventurers. The only exit is to the south."""),
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

player = Player('You', room['outside'])

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

    print(Room.__str__(player.current_room))
    print("this is current room items", player.current_room.items)
    print("this is players items", player.inventory)

    action = input("Input an action: ")
    if action[0] == "q":
        exit()
        print("Bye!")

    elif action[0] == "n":
        if player.current_room.n_to == None:
            print("\nNothin' over there. Pick a new direction")
        else:
            player.moveRoom(player.current_room.n_to)
    
    elif action[0] == "e":
        if player.current_room.e_to == None:
            print("\nNothin' over there. Pick a new direction")
        else:
            player.moveRoom(player.current_room.e_to)

    elif action[0] == "s":
        if player.current_room.s_to == None:
            print("\nNothin' over there. Pick a new direction")
        else:
            player.moveRoom(player.current_room.s_to)

    elif action[0] == "w":
        if player.current_room.w_to == None:
            print("\nNothin' over there. Pick a new direction")
        else:
            player.moveRoom(player.current_room.w_to)

    elif action == "take":
        if len(player.current_room.items) == 0:
            print("What are you trying to grab? There's nothing here.")
        else:
            for item in player.current_room.items:
                player.current_room.removeItem(item)
                player.addItemToInventory(item)
    
    elif(action == 'drop'):
        if len(player.inventory) == 0:
            print("Nothing in your inventory to drop. To view inventory, enter 'i' or 'inventory'.")
        else:
            for item in player.inventory:
                player.current_room.addItem(item)
                player.removeItemFromInventory(item)

    elif(action[0] == 'i' or action == 'inventory'):
        for item in player.inventory:
            print(item.name)

    else:
        print("\nyou must use, 'n', 'e', 's', and 'w'")

    