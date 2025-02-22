from .item import Item

class Vendor:
    def __init__(self, inventory = None):
        if not inventory:
            inventory = []
        self.inventory = inventory

    def add(self, item):
        self.inventory.append(item)
        return item

    def remove(self, item):
        if item not in self.inventory:
            return False
        self.inventory.remove(item)
        return item

    def get_by_category(self, category):
        items = []

        for item in self.inventory:
            if item.category == category:
                items.append(item)
        return items

    def get_by_newest(self):
        if self.inventory:
            newest_item = self.inventory[0]
            for item in self.inventory:
                if item.age < newest_item.age:
                    newest_item = item
            return newest_item
        return None

    def swap_items(self, swapee, my_item, their_item):
        if my_item in self.inventory and their_item in swapee.inventory:
            swapee.add(my_item)
            self.add(their_item)
            swapee.remove(their_item)
            self.remove(my_item)
            return True
        return False

    def swap_first_item(self, swapee):
        if self.inventory and swapee.inventory:
            my_item = self.inventory[0]
            their_item = swapee.inventory[0]
            
            self.add(their_item)
            swapee.add(my_item)
            self.remove(my_item)
            swapee.remove(their_item)
            return True
        return False

    def get_best_by_category(self, category):
        category_items = self.get_by_category(category)
        
        if not category_items:
            return None
        
        best_item = category_items[0]
        for item in category_items:
            if item.condition > best_item.condition:
                best_item = item
        
        return best_item

    def swap_best_by_category(self, other, my_priority, their_priority):
        swapee_best_item = other.get_best_by_category(my_priority)
        my_best_item = self.get_best_by_category(their_priority)
        
        if my_best_item and swapee_best_item:
            self.swap_items(other, my_best_item, swapee_best_item)
            return True
        return False

    def swap_by_newest(self, other):
        my_newest_item = self.get_by_newest()
        swapee_newest_item = other.get_by_newest()

        if my_newest_item and swapee_newest_item:
            self.swap_items(other, my_newest_item, swapee_newest_item)
            return True
        return False
