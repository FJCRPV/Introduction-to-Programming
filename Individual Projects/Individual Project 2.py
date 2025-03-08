'''

Course: Introduction to Programming
Author: Francisco Perestrello
Student number: 39001
Year: 2020

'''
# ---------------------------------------------- Let's start by the game logic ---------------------------------------------------------- #

import random

suits = ['Hearts', 'Diamonds', 'Spades', 'Clubs']
ranks = ['Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace']
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
         'Queen':10, 'King':10, 'Ace':11}

global playing
playing = True
                         #Creating the classes
class Card(): 
    
    def __init__(self, suit, rank):  #Attributing suits and ranks to the cards
        self.suit = suit
        self.rank = rank
    
    def __str__(self):
        return self.rank + " of " + self.suit  #Defining how the cards are printed
    
class Deck():
    
    def __init__(self):
        self.deck = [] #Start with an empty list
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit, rank)) #Build a card object for each combination of suit and rank and add them to the list
                
    def __str__(self):
        deck_comp = " "  #Start with an empty string
        for card in self.deck:
            deck_comp += "\n" + card.__str__()  #Add each card object's print string
        return "The deck has: " + deck_comp
    
    def shuffle(self):  #Shuffle the deck
        random.shuffle(self.deck)
        
    def deal(self):  #Deal the cards to the player/dealer, while taking them out of the deck list
        single_card = self.deck.pop()
        return single_card

class Hand():
    
    def __init__(self):
        self.cards = []  #Start with an empty list as we did in the Deck class
        self.value  =0  #Start with zero value
        self.aces = 0  #Sdding an attribute to keep track of aces
        
    def add_card(self, card):
        self.cards.append(card)  #Adding a card into the card list embeded into the Hand class
        self.value += values[card.rank]
        if card.rank == "Ace":
            self.aces +=1  #Add 1 to the self.aces constructor

    def adjust_for_ace(self):
        while self.value>21 and self.aces>0:  #If the hand value is over 21, aces are now valued at 1 instead of 11
            self.value -= 10  
            self.aces -= 1
            
class Chips():
    
    def __init__(self):
        self.total = 100 #let's make it default
        self.bet = 0
        
    def win_bet(self):  #Winning adds your bet to your total
        self.total += self.bet
    
    def lose_bet(self):  #Losing takes your bet from your total
        self.total -= self.bet
        
def take_bet(chips):
    
    print("\nTotal of chips: ", player_chips.total)  #Inform the player of his total number of chips
    while True:
        try:
            chips.bet = int(input("Please enter your bet: "))   #Ask for the bet
        except ValueError:
            print("You are only allowed integer bets.")
        else:
            if chips.bet > chips.total:
                print ("Sorry! You don't have enough chips to play that amount.")
            else:
                break

        
def hit(deck, hand):  #Adding the hit function
    
    hand.add_card(deck.deal())
    hand.adjust_for_ace()    
    
def hit_or_stand(deck, hand):  #Asking the player if he wishes to hit or stand
    
    global playing
    while playing == True:
        print("\nWould you like to Hit or Stand?\n1. Hit\n2. Stand")
        x = int(input("Please select an option: "))
        if x==1:
            hit(deck, hand)  #If the palyer wishes to hit, we call the hit function
        elif x==2:
            playing = False  #Turning the global variable false so we exit the loop
        else:
            print("Please select a valid option.")
            continue
        break
    
def show_some(player, dealer):  #Showing the table's cards, while keeping one of the dealer's cards hidden
    
    print("\n----------------------------------------------------------")
    print("\nDealer's Hand: \n")
    print(dealer.cards[1])
    print("### ## ###")
    print("\n\nPlayer's Hand: \n", *player.cards, sep = "\n") #I found that instead of redefining the print function, to print all the 
    print("\nPoints: ", player.value)                        #objects inside a list (unpacking), we only have to put an * before calling it
    print("\n----------------------------------------------------------")
        
def show_all(player, dealer):  #Showing all the cards on the table
    
    print("\n----------------------------------------------------------")
    print("\nDealer's Hand: \n", *dealer.cards, sep = "\n")
    print("\nPoints: ", dealer.value)
    print("\n\nPlayer's Hand: \n", *player.cards, sep = "\n")
    print("\nPoints: ", player.value)
    print("\n----------------------------------------------------------")
    
def player_busts(player, dealer, chips):  #Five functions for the five possible outcomes of the game
    print("\nPlayer busts!\nYou lose.")
    chips.lose_bet()

def player_wins(player, dealer, chips):
    print("\nPlayer wins!\nYou win!")
    chips.win_bet()
    
def dealer_busts(player, dealer, chips):
    print("\nDealer busts!\nYou win!")
    chips.win_bet()
    
def dealer_wins(player, dealer, chips):
    print("\nDealer wins!\nYou lose.")
    chips.lose_bet()
    
def tie(player, dealer):
    print("\nTie!")
    
# ----------------------------------------------------- Now onto the game code ---------------------------------------------------------- #
    
print ("\nWelcome to the Casino!\nToday we are playing blackjack.") #Print an opening statement. It is done outside of the loop because
                                                                    #otherwise it would pop up every time the player chooses "Play Again"
player_chips = Chips()  #Set up the player's chips. It is done outside of the loop because otherwise after "Play again", the chips would be
                        #set back to 100
while True:
    
    deck = Deck()  #Create a deck
    deck.shuffle()  #Shuffle the deck
    
    take_bet(player_chips)  #Call the bet function
    
    player_hand = Hand()  #Set the player's hand
    player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())
    
    dealer_hand = Hand()  #Set the dealer's hand
    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())
    
    show_some(player_hand, dealer_hand)  #Show cards (but keep one dealer card hidden)
    
    while playing:
        
        hit_or_stand(deck, player_hand)  #Ask the player if they want to hit or stand
        
        show_some(player_hand, dealer_hand)  #Show cards after the player's decision but before the dealer plays (to see the state of the
                                             #game before the dealer starts taking hits) #One dealer card is still hidden
        if player_hand.value>21:  #If the player's hand exceeds 21, run player_busts and break the loop
            player_busts(player_hand, dealer_hand, player_chips)  #If the player busts, there is no need to show the dealer's cards
            break
        
    if player_hand.value<=21:  #If the player hasn't busted, play Dealer's hand until he reaches 17
        while dealer_hand.value<17:
            hit(deck, dealer_hand)
        
        show_all(player_hand, dealer_hand) #Show all the cards
        
        if dealer_hand.value>21:  #Run the different winning scenarios
           dealer_busts(player_hand, dealer_hand, player_chips)
           
        elif dealer_hand.value > player_hand.value:
            dealer_wins(player_hand, dealer_hand, player_chips)
            
        elif dealer_hand.value < player_hand.value:
            player_wins(player_hand, dealer_hand, player_chips)
            
        else:
            tie(player_hand, dealer_hand)
            
    print("\nTotal of chips:", player_chips.total)  #Inform player of their chips total

    if player_chips.total==0:  #If the player lost all his chips, the game ends
        print("\nYou lost all your chips.\nThank you for playing!")
        break
    
    print("\nPlay again?\n1. Yes\n2. No")  #Ask to play again
    play_again =int(input("Please select an option: "))
    
    if play_again == 1:
        playing = True
        continue
    
    elif play_again == 2:
        print("\nThank you for playing!")
        break
    
    else:
        print("Please select a valid option")