class ItemAmmo:

    def __init__(self, name, count):
        self._name = name
        self._count = count
        self._type = "ItemAmmo"

    def get_name(self):
        return self._name

    def get_count(self):
        return self._count

    def add_ammo(self, count):
        self._count += count

    def remove_ammo(self, count):
        self._count -= count