from swap_meet.item import Item


class Decor(Item):
    def __init__(self, condition: float=0, age: int=100): 
        super().__init__(category="Decor", condition=condition, age=age)

    def __str__(self):
        return ("Something to decorate your space.")