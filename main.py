from datetime import date, timedelta
from board import Board
from issue import Issue
from task import Task
from user import User


def add_days_to_now(d):
    return date.today() + timedelta(days=d)

tsk = Task("test123","ivanuuuuu",add_days_to_now(1))
tsk1 = Task("test123","ivanuuuuu",add_days_to_now(1))
tsk1.advance_status()
tsk2 = Task("test123","ivanuuuuu",add_days_to_now(1))
tsk2.advance_status()
tsk2.advance_status()
usr = User("Ivan","ivan@ivan.com",[tsk,tsk,tsk2])
print(usr.capacity)
