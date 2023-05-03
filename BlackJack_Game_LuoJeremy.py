
#IDLE Open Source
#Note to Viewer: The "deal_cards function" is used at the beginning of the game to deal two cards each to the player and the dealer. One of the dealer's cards is hidden, and the other is shown to the player.
#The "calculate_total" function takes a list of cards as input and returns the total value of those cards. If the list includes an ace, which can be worth 1 or 11, the function uses the value that results in the highest total without exceeding 21.
#The "display_results" function is called after the player has decided to stay and the dealer has taken all necessary cards. The function calculates the total values for both the player and the dealer, and then prints a message indicating the winner (or a tie).
#The main game loop repeatedly asks the player to hit or stay until the player either reaches 21 points or goes bust. Once the player decides to stay, the dealer automatically takes more cards until their total is 17 or more. If the dealer goes bust, the player wins. Otherwise, the display_results function is called to determine the winner. The game ends once the winner is determined.



import random

#list of the card values
cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

#empty lists in order to hold onto player and dealer cards
player_cards = []
dealer_cards = []

#function to deal cards to each player
def deal_cards():
    for i in range(2):
        player_cards.append(random.choice(cards))
        dealer_cards.append(random.choice(cards))
    print("Here are the dealer’s cards: {} X".format(dealer_cards[0]))

#function to calculate the total value of a hand
def calculate_total(cards):
    total = sum(cards)
    if 11 in cards and total > 21:
        cards.remove(11)
        cards.append(1)
        total = sum(cards)
    return total

#function to print out the winner of the game
def display_results():
    player_total = calculate_total(player_cards) # Calculate total value of player's hand
    dealer_total = calculate_total(dealer_cards) # Calculate total value of dealer's hand
    print("The Player has {} and the Dealer has {}.".format(player_total, dealer_total))
    if player_total == dealer_total:
        print("It's a tie!")
    elif player_total > 21:
        print("The Player is bust! The Dealer wins!")
    elif dealer_total > 21:
        print("The Dealer is bust! The Player wins!")
    elif player_total > dealer_total:
        print("The Player wins!")
    else:
        print("The Dealer wins!")

#call for the function to deal cards to the player
deal_cards()

#a "while" loop that will continue until a player wins or busts
while True:
    player_total = calculate_total(player_cards)
    dealer_total = calculate_total(dealer_cards)
    print("Turn: Player")
    print("Here are your cards: {}".format(player_cards))
    if player_total == 21:
        print("The Player has 21!")
        print("The Player wins!")
        break
    elif player_total > 21:
        print("The Player goes bust! The Dealer wins!")
        break
    else:
        hit_or_stay = input("What would you like to do? (Hit/Stay) ") # prompt the user to choose to hit or stay
        if hit_or_stay.lower() == "hit":
            player_cards.append(random.choice(cards))
        else:
            print("Turn: Dealer")
            print("Here are your cards: {}".format(dealer_cards))
            while dealer_total <= 16:
                dealer_cards.append(random.choice(cards))
                dealer_total = calculate_total(dealer_cards)
                print("Your cards total to 16 or less. You must take another card.")
                print("Here are you cards: {}".format(dealer_cards))
                
            #print("Turn: Dealer")
            #print("Here are your cards: {}".format(dealer_cards))
            if dealer_total > 21:
                print("The Dealer goes bust!")
                print("The Player wins!")
            else:
                display_results()  # if neither the dealer or player busts, determine the winner using the "display_results()" function
            break
