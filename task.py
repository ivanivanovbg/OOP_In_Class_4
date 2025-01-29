from board_item import BoardItem
from datetime import date
from item_status import ItemStatus


class Task(BoardItem):
    def __init__(self, title: str, assignee: str, due_date: date):
        super().__init__(title, due_date, ItemStatus.TODO)
        self._ensure_valid_assignee(assignee)
        self._assignee = assignee

    @property
    def assignee(self):
        if hasattr(self,"_asssignee"):
            return self._assignee

    @assignee.setter
    def assignee(self, value):
        self._ensure_valid_assignee(value)
        if hasattr(self,"_asssignee"):
            self._log_event(f'Assignee changed from {self._assignee} to {value}')

        self._assignee = value

    def info(self):
        return f'Task (assigned to: {self.assignee}) {super().info()}'

    def _ensure_valid_assignee(self, title):
        if (len(title) < 5 or len(title) > 30):
            raise ValueError('Illegal title length [5:30]')

