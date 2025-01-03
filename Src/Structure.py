

class Structure:
    """
    It represents a block of the chapter.
    Every chapter is composed by a fixed number of blocks.
    """
    def __init__(self):
        self.order_block = 0
        self.items = []
        self.active = False
