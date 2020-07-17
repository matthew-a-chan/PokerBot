class Card(object):
    suit = ""
    rank = 0


    
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def get_suit(self):
         return self.suit
    
    def get_rank(self):
        return self.rank
