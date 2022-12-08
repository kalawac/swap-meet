from swap_meet.item import Item


class Electronics(Item):
    def __init__(self, condition: float=0, age: int=100): 
        super().__init__(category="Electronics", condition=condition, age=age)

    def __str__(self):
        return ("A gadget full of buttons and secrets.")
