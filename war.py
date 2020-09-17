from deck import Deck
from player import Player

player_one = Player(input("Enter Name of Player 1 : "))
player_two = Player(input("Enter Name of Player 2 : "))

new_deck = Deck()
new_deck.shuffle_cards()

for i in range(26):
    player_one.add_cards(new_deck.deal_one())
    player_two.add_cards(new_deck.deal_one())

game_on = True
round_num=0

while game_on:

    round_num += 1
    print(f"Round {round_num}")

    if len(player_one.all_cards) == 0:
        print(f"{player_one.name} is out of Cards !!!! {player_two.name} is the winner !")
        game_on = False
        break

    if len(player_two.all_cards) == 0:
        print(f"{player_two.name} is out of Cards !!!! {player_one.name} is the winner !")
        game_on = False
        break

    player_one_cards = []
    player_one_cards.append(player_one.remove_one())

    player_two_cards = []
    player_two_cards.append(player_two.remove_one())

    at_war = True

    while at_war:

        if player_one_cards[-1].value > player_two_cards[-1].value:

            player_one.add_cards(player_one_cards)
            player_one.add_cards(player_two_cards)

            at_war = False

        elif player_one_cards[-1].value < player_two_cards[-1].value:

            player_two.add_cards(player_one_cards)
            player_two.add_cards(player_two_cards)

            at_war = False

        else:

            print("@ WAR !!!")

            """
            The number of cards that have to be drawn is set to 5 here , This can be varied
            according to the player's choice....
            """

            if len(player_one.all_cards) < 5:

                print(f"{player_one.name} can't declare war")
                print(f"{player_two.name} wins !!!!")

                game_on = False
                break

            elif len(player_two.all_cards) < 5:

                print(f"{player_two.name} can't declare war")
                print(f"{player_one.name} wins !!!!")

                game_on = False
                break

            else:
                for i in range(5):
                    player_one_cards.append(player_one.remove_one())
                    player_two_cards.append(player_two.remove_one())


