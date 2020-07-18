

from functools import total_ordering



@total_ordering
class Hand():

    def __init__(self, player, cards, table):
        self.player = player
        self.cards = cards
        self.table = table


    def __repr__(self):
        return f'Player: {self.player}, Cards: {self.cards}, Table: {self.table}'

# So we must implement these two methods: 
# __eq__ being the equality method (two hands evaluatate to the same)
# __lt__ being the less than method (`self` is a worse hand than `other`)

# Note: we may assume that when these functions are called,
# `self.hand` will ALWAYS have 2 cards, and `self.table` will ALWAYS have 5 cards.

    def __eq__(self, other):
        return False


    def __lt__(self, other):
        return False