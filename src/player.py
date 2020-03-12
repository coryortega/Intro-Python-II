# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room
        self.inventory = []

    def moveRoom(self, room):
        self.current_room = room
        # if getattr(self.current_room, f"{direction}_to"):
        #     self.current_room = getattr(self.current_room, f"{direction}_to")
        #     print(self.current_room)
        # else:
        #     print("You cannot move in that direction")
    
    def addItemToInventory(self, item):
        item.take_item()
        self.inventory.append(item)
        print(f"You added {item.name}")

    def removeItemFromInventory(self, item):
        item.drop_item()
        self.inventory.remove(item)
        print(f"You removed {item.name}")