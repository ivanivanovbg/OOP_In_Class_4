from boarditems.board_item import BoardItem
from datetime import date
from boarditems.item_status import ItemStatus
import user.user as user


class Task(BoardItem):
    def __init__(self, title: str, assignee, due_date: date):
        if not isinstance(assignee, user.User):
            raise ValueError("Invalid user supplied as assignee!")
        super().__init__(title, due_date, ItemStatus.TODO)
        self._ensure_valid_assignee(assignee.username)
        self.assignee = assignee

    @property
    def assignee(self):
        if hasattr(self,"_assignee"):
            return self._assignee

    @assignee.setter
    def assignee(self, value):
        if isinstance(value, user.User):
            self._ensure_valid_assignee(value.username)
            if hasattr(self,"_assignee"):
                self._log_event(f'Assignee changed from {self._assignee} to {value.username}')
            self._assignee = value.username

    def info(self):
        return f'Task (assigned to: {self.assignee}) {super().info()}'

    def _ensure_valid_assignee(self, title):
        if (len(title) < 5 or len(title) > 30):
            raise ValueError('Illegal title length [5:30]')

    def __eq__(self,other):
        if not isinstance(other,type(self)):
            return False
        else:
            if (self.assignee == other.assignee and
                self.status == other.status and
                self.title == other.title and
                self.due_date == other.due_date):
                return True
            else:
                return False

