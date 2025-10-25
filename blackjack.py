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
    """Draws num_cards cards and appends them to the given hand (or creates a new one)."""
    hand = []
    for _ in range(num_cards):
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

def display_hand(hand, is_dealer=False, reveal_all=False):
    """Displays the hand. If dealer and not revealing all, only show one card."""
    print("Dealer's hand:" if is_dealer else "Your hand:")

    for i, (rank, suit) in enumerate(hand):
        if is_dealer and not reveal_all and i > 0:
            print("Hidden card")
        else:
            print(f"{rank} of {suit}")

# Draw the hand for player, and dealer
player_hand = draw_hand(2)
dealer_hand = draw_hand(2)

display_hand(player_hand, False, True)
print("\n")
display_hand(dealer_hand, True, False)

choice = None

# Simulates a game of blackjack on the player side, evaluates multiple conditions for continuing or stopping the player's turn.
while choice is not "S":
    if evaluate_hand(player_hand) == 21:
        print("Blackjack!")
        break
    elif choice == "S":
        print(f"You have decided to stay. You're total value is {evaluate_hand(player_hand)}")
        break
    elif evaluate_hand(player_hand) > 21:
        print("You bust!")
        break
    elif choice == "H":
        player_hand.append(draw_card())
    else:
        choice = input(f"\nYou're current hand value is {evaluate_hand(player_hand)}, would you like to hit (H) or stay (S): ").upper()