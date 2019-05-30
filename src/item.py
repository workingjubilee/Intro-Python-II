class Item:
    def __init__(self, noun, description):
        self.noun = noun
        self.description = description

     #    * Hint: the name should be one word for ease in parsing later.

  # * This will be the _base class_ for specialized item types to be declared
  #   later.


# * Implement support for the verb `get` followed by an `Item` name. This will be
#   used to pick up `Item`s.

#   * If the user enters `get` or `take` followed by an `Item` name, look at the
#     contents of the current `Room` to see if the item is there.

#      * If it is there, remove it from the `Room` contents, and add it to the
#        `Player` contents.

#      * If it's not there, print an error message telling the user so.

#      * Add an `on_take` method to `Item`.

#         * Call this method when the `Item` is picked up by the player.

#         * `on_take` should print out "You have picked up [NAME]" when you pick up an item.

#         * The `Item` can use this to run additional code when it is picked up.

#      * Add an `on_drop` method to `Item`. Implement it similar to `on_take`.
