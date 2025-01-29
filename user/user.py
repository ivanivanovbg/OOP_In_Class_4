import boarditems.task as task
import re
from boarditems.item_status import *
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
    def capacity(self)->int:
        cap = 3 - len( [t.title for t in self.__atasks if (t.status == ItemStatus.TODO) or (t.status == ItemStatus.IN_PROGRESS) ])
        if cap >= 0:
            return cap
        else:
            return 0

    def __init__(self,username:str,email:str,assigned_tasks=[]):
        if len(username) > 0:
            self.__username = username
        else:
            raise ValueError("Username length must be greater than 0!")
        for tsk in assigned_tasks:
            if not isinstance(tsk, task.Task):
                raise ValueError("Task list contains invalid items!")
        self.email = email
        if len( [t.title for t in assigned_tasks if (t.status == ItemStatus.TODO) or (t.status == ItemStatus.IN_PROGRESS) ]) <= 3:
            self.__atasks = assigned_tasks[:]
        else:
            raise ValueError("Tasks with status TODO or IN_PROGRESS are more than 3!")

    def advance_task_status(self,tsk):
        if not isinstance(tsk, task.Task):
            raise ValueError("Not a valid task provided as argument to advance_task_status!")
        if tsk.status in [ItemStatus.TODO,ItemStatus.IN_PROGRESS]:
            for i_tsk in self.__atasks:
                if i_tsk == tsk:
                    i_tsk.advance_status()

    def receive_task(self,tsk):
        if isinstance(tsk, task.Task):
            if self.capacity == 0:
                raise ValueError("Maximum capacity exceeded !")
            else:
                self.__atasks.append(tsk)
        else:
            raise ValueError("tsk parameter is not a valid Task !")

    def remove_task(self,tsk):
        if isinstance(tsk, task.Task):
            if tsk in self.__atasks:
                self.__atasks.remove(tsk)
            else:
                raise ValueError("Task is not in the list!")
        else:
            raise ValueError("tsk parameter is not a valid Task !")

    def __eq__(self,other):
        if not isinstance(other,type(self)):
            raise ValueError("Second parameter is not a User")
        else:
            if self.username == other.username and self.email == other.email:
                return True
            else:
                return False


