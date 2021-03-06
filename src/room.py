# Implement a class to hold room information. This should have name and
# description attributes.


class Room:
    def __init__(self, name, description, n_to=0, s_to=0, e_to=0, w_to=0):
        self.name = name
        self.description = description
        self.n_to = n_to
        self.s_to = s_to
        self.e_to = e_to
        self.w_to = w_to
        self.item = []

    def __str__(self):
        info = f'{self.name}: {self.description}: {self.item}'
        return info

    def add_item(self, item):
        self.item.append(item)

    def remove_item(self, item):
        self.item.remove(item)

    def list_item(self, item):
        if len(self.item) > 0:
            print('Room items: ')
            for i in self.item:
                print(i.name)
        else:
            print('This room does not contain any items')

# NOTES
# GUIDED SOLUTION FROM THE LECTURE

# class Room:
#     '''
#     This is a room class
#     '''
#     def __init__(self, title, description):
#         self.title = title
#         self.description = description
#         self.n_to = None
#         self.s_to = None
#         self.e_to = None
#         self.w_to = None
#     def __str__(self):
#         '''
#         This is a string method
#         '''
#         return f"{self.title}\n\n{self.description}"
