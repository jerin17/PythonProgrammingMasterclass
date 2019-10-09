import random

try:
    import tkinter
except ImportError:
    import Tkinter as tkinter

def loadImages(cardImages):
    suits = ['hearts', 'clubs', 'diamonds', 'spades']
    faceCards = ['jack', 'queen', 'king']

    for suit in suits:
        for card in range(1, 11):
            name = 'cards_png/{}_of_{}.png'.format(str(card), suit)
            image = tkinter.PhotoImage(file=name)
            image = image.subsample(5)
            cardImages.append((card, image,))

        for card in faceCards:
            name = 'cards_png/{}_of_{}.png'.format(str(card), suit)
            image = tkinter.PhotoImage(file=name)
            image = image.subsample(5)
            cardImages.append((10, image,))


def dealCard(frame):
    # pop next card off the top of the deck
    nextCard = deck.pop(0)
    # and add it to back of the pack
    deck.append(nextCard)
    # add image to a label and add image
    tkinter.Label(frame, image=nextCard[1], relief='raised').pack(side='left')
    return nextCard

def scoreHand(hand):
    # calculate total score of all cards in list
    # only one ace can have value 11, and this will reduce to 1 if the hand would bust
    score = 0
    ace = False
    for nextCard in hand:
        cardValue = nextCard[0]
        if cardValue == 1 and not ace:
            ace = True
            cardValue = 11
        score += cardValue
        # if we would bust, check if there's an ace
        if score > 21 and ace:
            score -= 10
            ace = False
    return score



def dealDealer():
    dealerScore = scoreHand(dealerHand)
    while 0 < dealerScore < 17:
        dealerHand.append(dealCard(dealerCardFrame))
        dealerScore = scoreHand(dealerHand)
        dealerScoreLabel.set(dealerScore)


    playerScore = scoreHand(playerHand)
    if playerScore > 21:
        resultText.set("Dealer Wins !!")
    elif dealerScore > 21 or dealerScore < playerScore:
        resultText.set("Player Wins !!")
    elif dealerScore > playerScore:
        resultText.set("Dealer Wins !!")
    else:
        resultText.set("Its a draw !")

def dealPlayer():
    playerHand.append(dealCard(playerCardFrame))
    playerScore = scoreHand(playerHand)
    playerScoreLabel.set(playerScore)
    if playerScore > 21:
        resultText.set("Dealer Wins")


def newGame():
    global dealerCardFrame
    global playerCardFrame
    global dealerHand
    global playerHand

    dealerCardFrame.destroy()
    dealerCardFrame = tkinter.Frame(cardFrame, background='green')
    dealerCardFrame.grid(row=0, column=1, sticky='ew', rowspan=2)

    playerCardFrame = tkinter.Frame(cardFrame, background='green')
    playerCardFrame.grid(row=2, column=1, sticky='ew', rowspan=2)
    resultText.set("")

    dealerHand = []
    playerHand = []

    dealPlayer()
    dealerHand.append((dealCard(dealerCardFrame)))
    dealerScoreLabel.set(scoreHand(dealerHand))
    dealPlayer()



# global playerScore
    # global playerAce
    #
    # cardValue = dealCard(playerCardFrame)[0]
    # if cardValue == 1 and not playerAce:
    #     playerAce = True
    #     cardValue = 11
    # playerScore += cardValue
    # # if we would bust, check if there's an Ace and subtract
    # if playerScore > 21 and playerAce:
    #     playerScore -= 10
    #     playerAce = False
    # playerScoreLabel.set(playerScore)
    # if playerScore > 21:
    #     resultText.set("Dealer Wins!")

mainwindow = tkinter.Tk()
# Set up screen and frames for the dealer and player
mainwindow.title("Black Jack")
mainwindow.geometry("640x480")
mainwindow.configure(background='green')


resultText = tkinter.StringVar()
result = tkinter.Label(mainwindow, textvariable=resultText)
result.grid(row=0, column=0, columnspan=3)

cardFrame = tkinter.Frame(mainwindow, relief="sunken", borderwidth=1, background="green")
cardFrame.grid(row=1, column=0, sticky='ew', columnspan=3, rowspan=2)

dealerScoreLabel = tkinter.IntVar()
tkinter.Label(cardFrame, text='Dealer', background='green', fg='white').grid(row=0, column=0)
tkinter.Label(cardFrame, textvariable=dealerScoreLabel, background='green', fg='white').grid(row=1, column=0)

# embedded frame to hold the card
dealerCardFrame = tkinter.Frame(cardFrame, background='green')
dealerCardFrame.grid(row=0, column=1, sticky='ew', rowspan=2)

playerScoreLabel = tkinter.IntVar()
playerScore = 0
playerAce = False


tkinter.Label(cardFrame, text='Player', background='green', fg='white').grid(row=2, column=0)
tkinter.Label(cardFrame, textvariable=playerScoreLabel, background='green', fg='white').grid(row=3, column=0)

# embedded frame to hold the player's card
playerCardFrame = tkinter.Frame(cardFrame, background='green')
playerCardFrame.grid(row=2, column=1, sticky='ew', rowspan=2)

buttonFrame = tkinter.Frame(mainwindow)
buttonFrame.grid(row=3, column=0, columnspan=3, sticky='w')

dealerButton = tkinter.Button(buttonFrame, text='Dealer', command=dealDealer)
dealerButton.grid(row=0, column=0)

playerButton = tkinter.Button(buttonFrame, text="Player", command=dealPlayer)
playerButton.grid(row=0, column=1)

newGameButton = tkinter.Button(buttonFrame, text='New Game', command=newGame)
newGameButton.grid(row=0, column=2)

# load cards
cards = []
loadImages(cards)
# print(cards)

# create a new dec of cards and shuffle them
deck = list(cards)
random.shuffle(deck)

# create list to store dealer's and player's hand

dealerHand = []
playerHand = []

dealPlayer()
dealerHand.append((dealCard(dealerCardFrame)))
dealerScoreLabel.set(scoreHand(dealerHand))
dealPlayer()

mainwindow.mainloop()