class Item:
    def __init__(self, category="", condition: float=0, age: int=100):
        self.category = category
        self.condition = condition
        self.age = age

    def __str__(self):
        return "Hello World!"

    def condition_description(self):
        CONDITION_DESCRIPTIONS = (
            "Not even good enough to recycle.",
            "Unusable, but you might still want it.",
            "Has some life left.",
            "Appropriately mediocre.",
            "Works well for what it is.",
            "Amaaaazing!",
        )
        
        if 0 <= int(self.condition) <=5:
            description_selector = int(self.condition)
        elif int(self.condition) < 0:
            description_selector = 0
        else:
            description_selector = 5

        return CONDITION_DESCRIPTIONS[description_selector]