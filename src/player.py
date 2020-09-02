# Write a class to hold player information, e.g. what room they are in
# currently.

class Player():
    def __init__(self, name, current_room, items=None, itemnames=None):
        self.name = name
        self.current_room = current_room
        self.items = []
        self.itemnames = {}


    def location(self):
        print(f"""Your current location: {self.current_room.name}. 
        \n{self.current_room.description}""")


    def move(self, movement):
        print(movement)
        try:
            # Take in movement and concat to attr name
            attribute = movement + '_to'
            # Update current room with new room
            self.current_room = getattr(self.current_room, attribute)
            print("\n>> You move into the next room...")
        
        except:
            print("\n>> You turn back because nothing is in that direction...")
        

    def add_item(self, new_item):
        # Manage inventories
        # Make sure item is in room
        if new_item in self.current_room.itemnames:
            # Add new_item  to player inventory
            item = self.current_room.itemnames[new_item]
            self.items.append(item)
            self.itemnames[new_item] = item
            item.on_take()
            # Remove new_item from the room inventory
            self.current_room.remove_items(new_item)
        else:
            print(f"There is no {new_item} for you to pick up.")


    def drop_items(self, removed_item):
        if removed_item in self.itemnames:
            # Remove items from player inventory
            item = self.itemnames[removed_item]
            self.items.remove(item)
            self.itemnames.pop(removed_item)
            item.on_drop()
        else:
            print(f"You can't drop an item you do not have.")



    def item_action(self, action, item_name):
        if action == 'take':
            self.add_item(item_name)

        elif action == 'drop':
            self.drop_items(item_name)

        elif action == 'check':
            self.get_player_items()

        else:
            print("Please input a valid command. 'take/drop' [item_name]")


    def get_player_items(self):
        # Return current player inventory
        if len(self.items) == 0:
            print("Your inventory is empty")
        
        else:
            print(f"You have {len(self.items)} in your inventory.")
            for idx, item in enumerate(self.items, 1):
                print(f"{idx}: {item.name} \n{item.description}")
    


    def __str__(self):
        return f'Name: {self.name} \nCurrent Room: {self.current_room}'
    

    def __repr__(self):
        return f'Player({self.name}, {self.current_room}) object'