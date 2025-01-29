from boarditems import task, item_status
from boarditems.board_item import BoardItem
from user import user


class Board():
    def __init__(self):
        self._items = []
        self.__users:list[user.User] = []

    def add_item(self, item: BoardItem):
        if item in self._items:
            raise ValueError('BoardItem already in the list')
        self._items.append(item)

    def add_user(self,username:str,email:str):
        usr = user.User(username, email)
        self.__users.append(usr)
        return usr

    def reassign_task(self,tsk,new_assignee):
        if not isinstance(tsk, task.Task):
            raise ValueError("Invalid task supplied for reassign_task method")
        if not isinstance(new_assignee, user.User):
            raise ValueError("Invalid user supplied for reassign_task method")
        if not tsk in self._items:
            raise ValueError("Task doesn't exist in boards!")
        if tsk.assignee == new_assignee.username:
            raise ValueError("Attempt to reassign task to same user!")
        for usr in self.__users:
            if tsk in usr.assigned_tasks:
                usr.remove_task(tsk)
            if usr == new_assignee:
                while not tsk.status == item_status.ItemStatus.TODO:
                    tsk.revert_status()
                tsk.assignee = usr
                usr.receive_task(tsk)

    @property
    def team_capacity(self):
        return sum([usr.capacity for usr in self.__users])

    @property
    def count(self):
        return len(self._items)
