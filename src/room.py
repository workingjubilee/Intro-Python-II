# Implement a class to hold room information. This should have name and
# description attributes.


class Room:
    def __init__(self, title, description, directions):
        self.title = title
        self.description = description
        self.directions = directions

        # The Room class should be extended with a list
        # that holds the Items that are currently in that room.

        # Add functionality to the main loop that prints out all
        # the items that are visible to the player when they are in that room.

        # * Make rooms able to hold multiple items
        # * Make the player able to carry multiple items
        # * Add items to the game that the user can carry around
        # * Add `get [ITEM_NAME]` and `drop [ITEM_NAME]` commands to the parser
