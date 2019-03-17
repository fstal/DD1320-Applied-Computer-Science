from linkedQFile import LinkedQ

def create_cardstack():
    """
    Function which creates our stack of cards based on user input.
    The used inputs values which are then used as value for each element in our queue
    i is a counter to count the number of elements in our queue
    """
    i = 0
    numinput = input('Choose numbers: ')
    numinput = numinput.split()
    for k in numinput:
        i = i +1
        cardstack.enqueue(int(k))
    return i


def magic_trick(counter):
    """
    Function which performs the magic trick.
    The for loop has to be twice as long as the queue since every other card is put in the back of the deck again.
    """
    for k in range(counter*2):
        if k == 0 or k % 2 == 0:                # Every other card is taken out of the queue and put back in at the back
            card = cardstack.dequeue()
            cardstack.enqueue(card)
        else:                                   # Every other card is taken out of the queue and written down
            poped_card = cardstack.dequeue()
            print(poped_card)


cardstack = LinkedQ()
counter = create_cardstack()
magic_trick(counter)



# 7 1 12 2 8 3 11 4 9 5 13 6 10 for card test
