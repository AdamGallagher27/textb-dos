
# this will define locations
# location will have
# name, description, close locations, items

class Location:
    def __init__(self, name, description, close_locat, items):
        self.name = name
        self.description = description
        self.close_locat = close_locat
        self.items = items