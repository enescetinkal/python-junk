#Gets mandatory stuff from cardlogic.py
from cardlogic import playingCard
from cardlogic import CARDCOLOR
from cardlogic import CARDID

import random

hand: list = []
pile: list = []

playerAmount: int = 0
turnWay: int = 1
currentTurn: int = 0

gameWon: bool = False

def main():
    global currentTurn
    if pile:
        print("Card at top of pile: " + pile[-1].color + " " + pile[-1].id + "\n")
    
    currentTurn = pickState(currentTurn)

    if len(hand[currentTurn]) == 0:
        print(f"Player {currentTurn} wins!")
    global gameWon
    gameWon = True


def checkCards(currentTurn):
    #Checks for every card for the current players hand.
    for i in hand[currentTurn]:
        if ((i.id == "Wild") or (i.id == "+4 Wild")) and (i.color != "Black"):
            print("card " + str(i) + " has a error.")
        else:
            print(i.color + " " + i.id)

def pickState(currentTurn):
    # You can pick a card to play or draw now
    checkCards(currentTurn)
    stateInput = input("What do you want to do? Play: P, Draw: D ")
    if (stateInput == "P") or (stateInput == "p"):
        cardInput = input("What card do you want to play? ")
        try:
            cardIndex = int(cardInput)
            selectedCard = hand[currentTurn][cardIndex]
            pile.append(selectedCard)
            del hand[currentTurn][cardIndex]
            handleCardEffect(selectedCard)
        except (TypeError, IndexError, ValueError):
            print("Incorrect number. Please try again.")

    elif (stateInput == "D") or (stateInput == "d"):
        hand[currentTurn].append(playingCard(random.randrange(0, 3), random.randrange(0, 14)))
    return nextTurn(currentTurn, turnWay)

def nextTurn(currentTurn, turnWay):
    currentTurn += turnWay
    if currentTurn >= playerAmount:
        currentTurn = 0
    elif currentTurn < 0:
        currentTurn = playerAmount - 1
    return currentTurn

def initGame(playerAmount):
    tempPlayerAmount = input("How many players do you want? ")
    if int(tempPlayerAmount) > 1:
        playerAmount = int(tempPlayerAmount)
            
        for i in range(playerAmount):
            hand.append([])

        for i in hand:
            for j in range(7):
                i.append(playingCard(random.randrange(0, 3), random.randrange(0, 14)))

def chooseColor(card):
    print("Choose a color: Red, Green, Blue, Yellow")
    while True:
        colorInput = input("Color: ").capitalize()
        if colorInput in CARDCOLOR[:4]:
            card.color = colorInput
            break
        else:
            print("Invalid color. Try again.")

def handleCardEffect(card):
    global currentTurn, turnWay, playerAmount

    if card.id == "Block":
        print("Next player is skipped!")
        currentTurn = nextTurn(currentTurn, turnWay)

    elif card.id == "Reverse":
        print("Turn order reversed!")
        turnWay *= -1
        if playerAmount == 2:
            currentTurn = nextTurn(currentTurn, turnWay)  # Acts like skip in 2-player game

    elif card.id == "+2":
        next_player = nextTurn(currentTurn, turnWay)
        print(f"Player {next_player} draws 2 cards!")
        for _ in range(2):
            hand[next_player].append(playingCard(random.randrange(0, 3), random.randrange(0, 13)))

    elif card.id == "Wild":
        chooseColor(card)

    elif card.id == "+4 Wild":
        chooseColor(card)
        next_player = nextTurn(currentTurn, turnWay)
        print(f"Player {next_player} draws 4 cards!")
        for _ in range(4):
            hand[next_player].append(playingCard(random.randrange(0, 3), random.randrange(0, 13)))


#Its a script guys
if __name__ == "__main__":
    initGame(playerAmount)

    while gameWon == False:
        main()

