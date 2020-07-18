from deck import Deck
from hand import Hand

class Game:

    phases = (("BET", ), ("TABLE", 3), ("BET", ), ("TABLE", 1), ("BET", ),
              ("TABLE", 1), ("BET", ))

    def __init__(self):
        pass

    def one_round(self, players):

        deck = Deck()
        table = []
        player_hands = {player: Hand(player, [], table) for player in players}
        pot = 0

        self.deal(player_hands, deck)
        print(player_hands)
        print(table)

        for phase in Game.phases:
            command, args = phase[0], phase[1:]
            if command == "BET":
                print('bet phase')
                pot += self.bet(players, player_hands, table)
            if command == "TABLE":
                print('table phase')
                num_cards = args[0]
                self.add_to_table(table, deck, num_cards)

            if len(players) < 2:
                # somebody won!
                print('exiting!')
                break

        self.resolve(players, player_hands, table, pot)

    def bet(self, players, player_hands, table):

        current_player = 0
        player_bets = {player: 0 for player in players}

        last_raised = -1
        max_bet = 0

        pot = 0

        while last_raised != current_player and len(players) > 1:

            print(player_hands[players[current_player]])
            bet = int(input())  #player.get_bet()#TODO: add args
            # TODO: remove money from player account

            if bet > max_bet or last_raised == -1:
                max_bet = bet
                last_raised = current_player

            pot += bet

            current_player += 1
            current_player %= len(players)

        return pot

    def deal(self, hands, deck):
        for hand in hands:
            hands[hand].cards += deck.get_cards(2)

    def add_to_table(self, table, deck, num_cards):
        table += deck.get_cards(num_cards)

    def resolve(self, players, player_hands, table, pot):
        winner = self.get_winner(players, player_hands, table)
        #TODO: Add money to winner

    def get_winner(self, players, player_hands, table):
        print(f'{players[0].name} Won!')
        return players[0]
        # TODO: make this work


class Player():
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return self.name



if __name__ == '__main__':
    A = Player("A")
    B = Player("B")
    C = Player("C")

    game = Game()

    game.one_round([A, B, C])
