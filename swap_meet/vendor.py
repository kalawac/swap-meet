from swap_meet.item import Item

class Vendor:
    def __init__(self, inventory=None):
        self.inventory = inventory if inventory else []

    def add(self, item):
        self.inventory.append(item)
        return item

    def remove(self, item):
        try:
            self.inventory.remove(item)
            return item

        except ValueError:
            return False

    def get_by_category(self, item_category):
        list_of_items = [item for item in self.inventory if item.category == item_category]

        return list_of_items

    def swap_items(self, vendor, item_s, item_v):
        
        if item_s not in self.inventory or item_v not in vendor.inventory:
            return False

        self.remove(item_s)
        vendor.add(item_s)
        vendor.remove(item_v)
        self.add(item_v)

        return True
        
    def swap_first_item(self, vendor):
        if not self.inventory or not vendor.inventory:
            return False

        item_s = self.inventory[0]
        item_v = vendor.inventory[0]

        return self.swap_items(vendor, item_s, item_v)

    def get_best_by_category(self, item_category):
        try:
            return max(self.get_by_category(item_category), key=lambda item: item.condition)
        
        except ValueError:
            return None

    def swap_best_by_category(self, other, my_priority, their_priority):
        item_s = self.get_best_by_category(their_priority)
        item_v = other.get_best_by_category(my_priority)

        return self.swap_items(other, item_s, item_v)

    def get_newest_by_category(self, item_category):
        try:
            return min(self.get_by_category(item_category), key=lambda item: item.age)
        
        except ValueError:
            return None

    def swap_by_newest(self, other, my_priority=None, their_priority=None):
        item_s = self.get_newest_by_category(their_priority) if their_priority else min(self.inventory, key=lambda item:item.age)
        item_v = other.get_newest_by_category(my_priority) if my_priority else min(other.inventory, key=lambda item:item.age)

        return self.swap_items(other, item_s, item_v)


