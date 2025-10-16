import random

def get_suit():
    """Returns a random playing card suit"""
    choice = random.randint(1, 4)

    if choice == 1:
        return "Hearts"
    elif choice == 2:
        return "Diamonds"
    elif choice == 3:
        return "Clubs"
    else:
        return "Spades"

def get_rank():
    """Returns a random playing card rank"""
    rank = random.randint(1, 13)

    if rank == 1:
        return "Ace"
    elif rank == 11:
        return "Jack"
    elif rank == 12:
        return "Queen"
    elif rank == 13:
        return "King"

    return str(rank)

def draw_card():
    """Returns a tuple representing a card (rank, suit)"""
    return (get_rank(), get_suit())

def draw_hand(num_cards):
    """Draws a random hand of cards as a list of (rank, suit) tuples"""
    hand = []
    for i in range(num_cards):
        hand.append(draw_card())
    return hand

def evaluate_card(rank):
    """Returns the value of a single card rank"""
    if rank in ["Jack", "Queen", "King"]:
        return 10
    elif rank == "Ace":
        return 11
    else:
        return int(rank)

def evaluate_hand(hand):
    """Returns the total value of the hand"""
    total = 0
    aces = 0
    for rank, suit in hand:
        value = evaluate_card(rank)
        total += value
        if rank == "Ace":
            aces += 1

    # Handle Aces counting as 1 if total > 21 (for Blackjack rules)
    while total > 21 and aces:
        total -= 10
        aces -= 1

    return total

# Example usage:
hand = draw_hand(2)
print("Your hand:")
for rank, suit in hand:
    print(f"{rank} of {suit}")

print("Total value:", evaluate_hand(hand))