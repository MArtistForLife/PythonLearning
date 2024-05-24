##---------------------##
print("EXERCISE 1")
print("Now we will play a game of Blackjack.")

import random

############ Rules ############
#unlimited deck
#no jokers
#jack, queen, king each count as 10
#ace can count as 11 until user's total goes over 21, at which point the ace starts getting counted as 1
#cards in the list have an equal probability of being drawn
#cards aren't removed from the deck as they're drawn

############ Steps ############
#detect when computer or user has a blackjack (ace + 10 value card)
#if computer gets blackjack, then user LOSES (even if user also has a blackjack)
#if user gets blackjack, then they win (UNLESS computer also has a blackjack)
#calculate user's and computer's scores based on their card values
#reveal computer's first card to user
#game ends immediately when user's score goes over 21 OR if the user or computer get a blackjack
#ask user if they want to get another card
#once user is done and no longer wants to draw any more cards, let computer play
#computer should keep drawing cards unless ITS score goes over 16
#compare user and computer scores and see if it's a win, loss, or draw
#print out player's and computer's final hand and their scores at the end of the game
#assume an infinite deck, so when card gets drawn, it is not removed from the deck

#append adds one element ALTOGETHER (even if it is its own list) to the end of a list
#extend adds each ELEMENT of an iterable (string, list, tuple) to the list

#create a dealCard() function that uses the cards list to return a random card
def dealCard():
    cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
    cardDrawn = random.choice(cards) #choose a random card from the cards list
    return cardDrawn

def compare(userPoints, computerPoints):
    if userPoints == computerPoints:
        return "Draw"
    elif computerPoints == 0:
        return "Lose, opponent has Blackjack!"
    elif userPoints == 0:
        return "You win with a Blackjack!"
    elif userPoints > 21:
        return "You went over, you lose :("
    elif computerPoints > 21:
        return "Opponent went over, you win :)"
    elif userPoints > computerPoints:
        return "You win!"
    else:
        return "You lose"

def playGame():
    #user and computer should each get dealt 2 cards using dealCard()
    userCards = [] #a list
    computerCards = [] #another list
    gameOver = False #in the beginning anyway

    for _ in range(2):
        userCards.append(dealCard()) #add to the existing list called userCards
        computerCards.append(dealCard()) #same but for computerCards

    def totalScore(cards):
        if sum(cards) == 21 and len(cards) == 2:
            return 0 #this way, we can determine if the user or computer got a score of blackjack 
            
        while 11 in cards and sum(cards) > 21:
            cards.remove(11)
            cards.append(1) #if the total score for either player goes over 21, the ace gets swapped out for a 1-pointer instead of 11
        
        return sum(cards) #sums all the elements in the list

    while not gameOver:
        userScore = totalScore(userCards)
        computerScore = totalScore(computerCards)
        print(f"Your cards: {userCards}, current Score: {userScore}")
        print(f"Computer's first card: {computerCards[0]}")

        if userScore == 0 or computerScore == 0 or userScore > 21:
            gameOver = True
        else:
            userDraws = input("Type 'yes' to get another card, type 'no' to pass: ")
            if userDraws == "yes":
                userCards.append(dealCard()) #get a card drawn and add to your user cards
            else:  
                gameOver = True

    while computerScore != 0 and computerScore < 17:
        computerCards.append(dealCard()) #add to the computer's overall hand of cards
        computerScore = totalScore(computerCards) #calculate score based on computer cards

    print(f"Your final hand: {userCards}, final score: {userScore}")
    print(f"Computer's final hand: {computerCards}, final score: {computerScore}")
    print(compare(userScore, computerScore))

while True:
    play = input("Do you want to play Blackjack? Type 'yes' or 'no': ")
    if play == "yes":
        playGame()
    elif play == "no":
        print("Okay, maybe next time!")
        break
    else:
        print("Invalid answer. Please just type 'yes' or 'no'.")
