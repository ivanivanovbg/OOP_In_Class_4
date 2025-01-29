from datetime import date, timedelta
from boards.board import Board
from boarditems.task import Task
from boarditems.issue import Issue
from boards.readonly_board import ReadonlyBoard
from boards.editable_board import EditableBoard


def add_days_to_now(d):
    return date.today() + timedelta(days=d)

issue = Issue('App flow tests?', 'We need to test the flow!', add_days_to_now(1))

readonly_board = ReadonlyBoard()
steven = readonly_board.add_user("Steven", "steven@asd.bg")
task = Task('Dont refactor anything', steven, add_days_to_now(2))

readonly_board.add_item(issue)  # method from CanAddItem
readonly_board.add_item(task)
print(readonly_board.count)  # 2     # property from Board

editable_board = EditableBoard()
editable_board.add_item(issue)  # method from CanAddItem
print(editable_board.count)
editable_board.remove_item(issue)  # method from CanRemoveItem
print(editable_board.count)  # 0     # property from Board