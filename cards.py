import random

suits = ["Hearts", "Clubs", "Spades", "Diamonds"]
ranks = range(1,14)
deck = [(rank, suit) for suit in suits for rank in ranks]

def printDeck(deck):
    for card in deck:
        print(card)

def randomShuffle(deck):
    shuffledDeck = []
    while deck:
        index = random.randint(0, len(deck) - 1)
        card = deck[index]
        shuffledDeck.append(card)
        deck.remove(card)
    return shuffledDeck

def riffleShuffle(deck):
    shuffledDeck = []
    index = random.randint(22,32)
    pile1 = deck[:index]
    pile2 = deck[index:]
    ratio = len(pile1) / (len(pile1) + len(pile2))
    
    while (ratio > 0) and (ratio < 1):
        ratio = len(pile1) / (len(pile1) + len(pile2) - 2)
        pileIndex = random.uniform(0,1)
        if pileIndex < ratio:
            shuffledDeck.append(pile1[0])
            pile1.pop(0)
        else:
            shuffledDeck.append(pile2[0])
            pile2.pop(0)
    shuffledDeck += pile1 + pile2
    return shuffledDeck

def main():
    newDeck = riffleShuffle(riffleShuffle(deck))
    printDeck(newDeck)

main()
