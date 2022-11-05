class ShoppingCart:

    def __init__(self, max_size=5):
        self.max_size = max_size
        self.item_list = []
        self.price_map = {
            "orange": 1,
            "apple": 2,
            "mango": 3
        }

    def add_item(self, item):
        if len(self.item_list) == self.max_size:
            raise OverflowError
        self.item_list.append(item)

    def get_size(self):
        return len(self.item_list)

    def get_items(self):
        return self.item_list

    def get_total(self):
        total = 0
        for item in self.item_list:
            total += self.price_map[item]
        return total

