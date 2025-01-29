from board_item import BoardItem


class Board:
    def __init__(self):
        self._items = []

    def add_item(self, item: BoardItem):
        if item in self._items:
            raise ValueError('BoardItem already in the list')

        self._items.append(item)

    @property
    def count(self):
        return len(self._items)
