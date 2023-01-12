class Deck:
    value = {
             'Two': 2,
             'Three': 3,
             'Four': 4,
             'Five': 5,
             'Six': 6,
             'Seven': 7,
             'Eight': 8,
             'Nine': 9,
             'Ten': 10,
             'Jack': 10,
             'Queen': 10,
             'King': 10,
             'Ace': 11
    }
    
    def __init__(self, value):
        self.value = value

class Hand:
    def __init__(self):
        self.cards = []
        
    def hand_value(self, card):
        result = 0
        ace = 0
        for card in self.cards:
            result += card.value
            if card.value == 1:
                ace += 1
        while result + 10 <= 21 and ace > 0:
            result += 10
            ace -= 1
        return result