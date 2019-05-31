# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
    def __init__(self, name, location, has_items=[]):
        self.name = name
        self.location = location
        self.has_items = has_items

    def inventory(self):
        print(self.has_items)

# * Add capability to add `Item`s to the player's inventory. The inventory can
#   also be a list of items "in" the player, similar to how Items can be in a
#   `Room`.
