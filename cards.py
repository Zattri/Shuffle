import random

suits = ["Hearts", "Clubs", "Spades", "Diamonds"]
ranks = list(range(1,11)) + ["Jack", "Queen", "King"]
deck = [(rank, suit) for suit in suits for rank in ranks]

def printDeck(deck):
    for card in deck:
        print(card[0], "of", card[1])

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
        if random.uniform(0,1) < ratio:
            shuffledDeck.append(pile1[0])
            pile1.pop(0)
        else:
            shuffledDeck.append(pile2[0])
            pile2.pop(0)
    shuffledDeck += pile1 + pile2
    return shuffledDeck

def overhandShuffle(deck):
    shuffledDeck = []
    while deck:
        index = random.randint(2,6)
        shuffledDeck = deck[:index] + shuffledDeck
        deck = deck[index:]
    return shuffledDeck

def chainShuffle(shuffleChain, deck):
    shuffledDeck = []
    for shuffle in shuffleChain:
        shuffledDeck = shuffle(deck)
    return shuffledDeck

def repeatShuffle(shuffle, deck, times):
    count = 0
    shuffledDeck = []
    while count < times:
        shuffledDeck = shuffle(deck)
        count += 1
    return shuffledDeck

def main():
    newDeck = chainShuffle([riffleShuffle, overhandShuffle], deck)
    printDeck(newDeck)

main()
