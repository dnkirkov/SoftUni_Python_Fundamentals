# A faro shuffle is a method for shuffling a deck of cards, in which the deck is split exactly in half.
# Then the cards in the two halves are perfectly interleaved,
# such that the original bottom card is still on the bottom and the original top
# card is still on top.
# For example, faro shuffling the list ['ace', 'two', 'three', 'four', 'five', 'six'] once, gives
# ['ace', 'four', 'two', 'five', 'three', 'six']
# Write a program that receives a single string (cards separated by space) and on the second line receives a count of
# faro shuffles that should be made. Print the state of the deck after the shuffle.
# Note: The length of the deck of cards will always be an even number.

deck = input().split()
shuffle_index = int(input())
left_deck = []
right_deck = []
each_deck_len = int(len(deck) / 2)

for index in range(shuffle_index):
    new_deck = []
    left_deck = deck[0:each_deck_len]
    right_deck = deck[each_deck_len:]
    for card in range(each_deck_len):
        new_deck.append(left_deck[card])
        new_deck.append(right_deck[card])
    deck = new_deck
print(deck)