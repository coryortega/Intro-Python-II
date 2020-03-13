# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, name, description, items = []):
        self.name = name
        self.description = description
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None
        self.items = items
    
    def __str__(self):
        items = ''

        if(len(self.items) > 0):
            items = 'There are some things here:\n'
            for item in self.items:
                items = items + f'{item.name}: {item.description}\n'
        return f'\n{self.name}:\n{self.description}\n\n{items}'
    
    def addItem(self, item):
        self.items.append(item)

    def removeItem(self, item):
        self.items.remove(item)