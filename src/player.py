# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room
        self.item = []

    def on_take(self, item):
        self.item.append(item)
        
    def on_drop(self, item):
        self.item.remove(item)

    def list_items(self, item):
        if len(self.item) > 0:
            print('Inventory: ')
            for i in self.item:
                print(i)
        else:
            print('You currently do not have any items')

# NOTES
# GUIDED SOLUTION FROM THE LECTURE
# class Player:
#     def __init__(self, name, starting_room):
#         self.name = name
#         self.current_room = starting_room
#     def travel(self, direction):
#         next_room = getattr(self.current_room, f"{direction}_to")
#         if next_room is not None:
#             self.current_room = next_room
#             print(self.current_room)
#         else:
#             print("You cannot move in that direction")
