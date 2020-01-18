class ItemKey:

    def __init__(self, name_text, description_text, pickup_text, use_text):
        self._name_text = name_text
        self._description_text = description_text
        self._pickup_text = pickup_text
        self._use_text = use_text
        self._type = 'ItemKey'

    def get_name(self):
        return self._name_text

    def get_description(self):
        return self._description_text

    def get_pickup_text(self):
        return self._pickup_text

    def get_use_text(self):
        return self._use_text
        