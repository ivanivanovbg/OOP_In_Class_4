class ItemStatus:
    OPEN = 'Open'
    TODO = 'Todo'
    IN_PROGRESS = 'In progress'
    DONE = 'Done'
    VERIFIED = 'Verified'

    _order = (OPEN, TODO, IN_PROGRESS, DONE, VERIFIED)

    @classmethod
    def next(cls, current):
        idx = cls._order.index(current)
        if idx < len(cls._order) - 1:
            return cls._order[idx + 1]
        else:
            return current

    @classmethod
    def previous(cls, current):
        idx = cls._order.index(current)
        if idx > 0:
            return cls._order[idx - 1]
        else:
            return current
