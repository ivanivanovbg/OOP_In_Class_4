from task import Task
import re
from item_status import *
class User():
    @property
    def username(self):
        return self.__username

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self,value):
        regex = ".+@.+"
        if re.search(regex,value):
            self.__email = value
        else:
            raise ValueError("Invalid email!")

    @property
    def assigned_tasks(self):
        return tuple(self.__atasks)

    @property
    def capacity(self):
        cap = 3 - len( [t.title for t in self.__atasks if (t.status == ItemStatus.TODO) or (t.status == ItemStatus.IN_PROGRESS) ])
        if cap >= 0:
            return cap
        else:
            return 0

    def __init__(self,username:str,email:str,assigned_tasks:list[Task]):
        if len(username) > 0:
            self.__username = username
        else:
            raise ValueError("Username length must be greater than 0!")
        self.email = email
        if len( [t.title for t in assigned_tasks if (t.status == ItemStatus.TODO) or (t.status == ItemStatus.IN_PROGRESS) ]) <= 3:
            self.__atasks = assigned_tasks[:]
        else:
            raise ValueError("Tasks with status TODO or IN_PROGRESS are more than 3!")

    def advance_task_status(self,tsk:Task):
        if tsk.status in [ItemStatus.TODO,ItemStatus.IN_PROGRESS]:
            tsk.advance_status()

