class Inventory:
    __capacity = 0

    def __init__(self, inventory):
        self.__capacity = inventory
        self.items = []

    def add_item(self, item):
        if len(self.items) < self.__capacity:
            self.items.append(item)
        else:
            return "not enough room in the inventory"

    def get_capacity(self):
        space = self.__capacity
        return space

    def __repr__(self):
        space_left = self.__capacity - len(self.items)
        if space_left < 0:
            space_left = 0
        return f"Items: {', '.join(self.items)}.\nCapacity left: {space_left}"


inventory = Inventory(2)
inventory.add_item("potion")
inventory.add_item("sword")
print(inventory.add_item("bottle"))
print(inventory.get_capacity())
print(inventory)