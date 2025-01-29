from boarditems.board_item import BoardItem
from datetime import date
from boarditems.item_status import ItemStatus


class Issue(BoardItem):
    def __init__(self, title: str, description: str, due_date: date):
        super().__init__(title, due_date, ItemStatus.OPEN)
        self._description = description if description else 'No description'

    @property
    def description(self):
        if hasattr(self,"_description"):
            return self._description
        else:
            return 'No description'

    def info(self):
        return f'Issue ({self.description}) {super().info()}'
