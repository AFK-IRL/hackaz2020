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

        self._items.append(new_item)

    # item: string name of item to remove
    # count: integer, only used if ammo, amnt to deduct from ammo
    def remove_item(self, item, count):
        for i in self._items:
            if i.get_name() == item.get_name():
                if item.get_type() == 'ItemAmmo':
                    if item.get_count <= 0:
                        self._items.remove(i)
                    else:
                        i.remove_ammo(count)
                else:
                    self._items.remove(i)