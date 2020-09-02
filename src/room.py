# Implement a class to hold room information. This should have name and
# description attributes.

class Room():
    def __init__(self, name, description, n_to=None, s_to=None, e_to=None, w_to=None, items=None, itemnames=None):
        self.name = name
        self.description = description
        self.items = []
        self.itemnames = {}

    def add_items(self, room_items):
        # Add new item to room inventory
        for item in room_items:
            self.items.append(item)
            self.itemnames[item.name] = item


    def get_room_items(self):
        print("You decide to look for items.")
        # Return room inventory
        if len(self.items) == 0:
            print("You search everywhere but find nothing of use...")

        else:
            print(f"You find {len(self.items)} in the room.")
            for idx, item in enumerate(self.items, 1):
                print(f"\n{idx}: {item.name} \n{item.description}")
                

    def remove_items(self, name):
        # get item to remove
        item = self.itemnames[name]
        # Remove from items
        self.items.remove(item)
        # Remove from items list
        self.itemnames.pop(name)

        print(f"The {name} was taken from the room...")

    def __str__(self):
        return f'Room Name: {self.name}, Description: {self.description}'
