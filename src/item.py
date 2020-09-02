# Write a class to hold item information

class Item():
    
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def on_take(self):
        print(f"You have picked up the {self.name}.")

    def on_drop(self):
        print(f"You have dropped the {self.name}.")
    
    def __str__(self):
        return f'Item Name: {self.name}, Descripton: {self.description}'

    def __repr__(self):
        return f'Item Name: {self.name}'