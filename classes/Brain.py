
# this will handle user state
# health
# location
# inventory

# also process commands
# limit commands to 
# go, look, take, inventory

class Brain:
    def __init__(self, starting_location):
        self.location = starting_location
        self.health = 20
        self.inventory = []

    def take(self, item):
        print('you took:' + item)
        self.inventory.append(item)

    def look(self):
        print(self.location.description)

    def inventory(self):
        print(' - Inventory -')
        for item in self.inventory:
            print(item.name)