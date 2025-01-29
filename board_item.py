from datetime import date
from item_status import ItemStatus
from event_log import EventLog


class BoardItem:
    def __init__(self, title: str, due_date: date, initial_status):
        self._ensure_valid_title(title)
        self._ensure_valid_due_date(due_date)

        self._title = title
        self._due_date = due_date
        self._status = initial_status
        self._history = []

        class_name = type(self).__name__

        self._log_event(f'{class_name} created: {self.info()}')

    @property
    def status(self):
        return self._status

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self._ensure_valid_title(value)
        self._log_event(f'Title changed from {self._title} to {value}')

        self._title = value

    @property
    def due_date(self):
        return self._due_date

    @due_date.setter
    def due_date(self, value):
        self._ensure_valid_due_date(value)
        self._log_event(f'DueDate changed from {self._due_date} to {value}')

        self._due_date = value

    def revert_status(self):
        prev = self._status
        self._status = ItemStatus.previous(self._status)
        self._log_status_change(prev, self._status)

    def advance_status(self):
        prev = self._status
        self._status = ItemStatus.next(self._status)
        self._log_status_change(prev, self._status)

    def info(self):
        return f'{self._title}, [{self._status} | {self._due_date}]'

    def history(self):
        return '\n'.join((log.info() for log in self._history))

    def _log_event(self, description: str):
        self._history.append(EventLog(description))

    def _log_status_change(self, prev: str, current: str):
        if prev == current:
            self._log_event(f'Cant change status, already at {current}')
        else:
            self._log_event(f'Status changed from {prev} to {current}')

    def _ensure_valid_title(self, title):
        if (len(title) < 5 or len(title) > 30):
            raise ValueError('Illegal title length [5:30]')

    def _ensure_valid_due_date(self, due_date):
        if (due_date < date.today()):
            raise ValueError('Due date cant be in the past.')
