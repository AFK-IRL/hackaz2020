class Inventory:

    def __init__(self):
        self._items = []


    # item: string name of the item to look for
    def get_item(self, item_name):
        for item in self._items:
            if item.get_name() == item_name:
                return item

        return None

    # item: an instance of ItemKey, ItemAmmo, ItemWeapon, etc.
    def add_item(self, new_item):
        if new_item.get_type() == 'ItemAmmo':
            for item in self._items:
                if new_item.get_name() == item.get_name():
                    item.add_ammo(item.get_count())
                    return
        self._items.append(item)