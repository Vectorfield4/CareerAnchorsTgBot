from data import CareerCategory

class Question():
    def __init__(self, index:int, text: str, category: CareerCategory):
        self.index = index
        self.text = text
        self.category = category
        self.answer = 0
    def __str__(self):
        return self.text