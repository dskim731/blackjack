class Deck:
    def __init__(self):
        deck = []
        
        self.suits = ["diamonds", "clubs", "hearts", "spades"]
        self.values = range(2, 15)
        # 11=jack, 12=queen, 13=king, 14=ace
        
        for suit in self.suits:
            for value in self.values:
                deck.append(f'{value}_of_{suit}')