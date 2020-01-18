import random

def create_deck():
    deck = {
        "Ace of Spades" : 1, "Two of Spades" : 2,
        "Three of Spades" : 3, "Four of Spades" : 4,
        "Five of Spades" : 5, "Six of Spades" : 6,
        "Seven of Spades" : 7, "Eight of Spades" : 8,
        "Nine of Spades" : 9, "Ten of Spades" : 10,
        "Jack of Spades" : 10, "Queen of Spades" : 10,
        "King of Spades" : 10,

        "Ace of Hearts" : 1, "Two of Hearts" : 2,
        "Three of Hearts" : 3, "Four of Hearts" : 4,
        "Five of Hearts" : 5, "Six of Hearts" : 6,
        "Seven of Hearts" : 7, "Eight of Hearts" : 8,
        "Nine of Hearts" : 9, "Ten of Hearts" : 10,
        "Jack of Hearts" : 10, "Queen of Hearts" : 10,
        "King of Hearts" : 10,
        
        "Ace of Diamonds" : 1, "Two of Diamonds" : 2,
        "Three of Diamonds" : 3, "Four of Diamonds" : 4,
        "Five of Diamonds" : 5, "Six of Diamonds" : 6,
        "Seven of Diamonds" : 7, "Eight of Diamonds" : 8,
        "Nine of Diamonds" : 9, "Ten of Diamonds" : 10,
        "Jack of Diamonds" : 10, "Queen of Diamonds" : 10,
        "King of Diamonds" : 10,
        
        "Ace of Clubs" : 1, "Two of Clubs" : 2,
        "Three of Clubs" : 3, "Four of Clubs" : 4,
        "Five of Clubs" : 5, "Six of Clubs" : 6,
        "Seven of Clubs" : 7, "Eight of Clubs" : 8,
        "Nine of Clubs" : 9, "Ten of Clubs" : 10,
        "Jack of Clubs" : 10, "Queen of Clubs" : 10,
        "King of Clubs" : 10,
    }

    return deck

def deal_cards(deck, num_cards):
    hand = {}
    for count in range(num_cards):
        key, value = random.choice(list(deck.items()))
        hand[key] = value
    print(hand)

    value = 0
    for key in hand:
        value += hand[key]

    print("Value of hand:", value)

def main():
    deck = create_deck()
    num_cards = None
    try:
        num_cards = int(input("How many cards should I deal?  "))

        check = 1 < num_cards < 52
        if not check:
            raise Exception("Number must be between 1 and 52")
    except ValueError:
        print("Must be a number.")
    except Exception as ex:
        print(ex)

    deal_cards(deck, num_cards)
    
    
if __name__ == "__main__":
    main()