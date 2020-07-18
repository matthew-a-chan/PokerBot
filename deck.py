
import random

from card import Card






class Deck():

    def __init__(self):

        self.deck = []
        self.shuffle()


    def __len__(self):
        return len(self.deck)

    # alias for __len__
    def length(self):
        return len(self)




    
    def shuffle(self):
        self.deck = [Card(suit, rank) for suit in Card.suits for rank in Card.ranks]
        random.shuffle (self.deck)

    def get_cards(self, number):
        if number > len(self.deck):
            print ("Error! tried to draw more cards then are remaining in the deck!")
        cards = self.deck[:number]
        self.deck = self.deck[number:]
        return cards

