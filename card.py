


class Card(object):

    # Constants!!! Don't change these or I will hunt you down
    self.suits = ('Spades', 'Hearts', 'Clubs', 'Diamonds')
    self.ranks = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13)

    suit = ""
    rank = 0


    
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def get_suit(self):
         return self.suit
    
    def get_rank(self):
        return self.rank