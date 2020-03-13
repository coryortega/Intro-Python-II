class Item:
    def __init__(self, name, description):
        self.description = description
        self.name = name
    
    def drop_item(self):
        print(f'Item {self.name} has been dropped.\n')

    def take_item(self):
        print(f'You picked up: {self.name}\n Description: {self.description}')