import boards.board as board
import boarditems.board_item as bi


class EditableBoard(board.Board):

    def __init__(self):
        super().__init__()

    def remove_item(self,item:bi.BoardItem):
        if item in self._items:
            self._items.remove(item)
        else:
            raise ValueError("Item not contained in list!")
