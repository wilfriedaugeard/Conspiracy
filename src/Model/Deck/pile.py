class Pile:
    def __init__(self):
        self.pile = []

    def addCard(self, card):
        self.pile.append(card)

    def display(self):
        for member in self.pile:
            member.display()
            
    # Getters
    def getPile(self):
        return self.pile