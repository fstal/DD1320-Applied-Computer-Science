from bintreeFile import Bintree
from bintreeFile import ParentNode
from linkedQFile import LinkedQ
import sys


def read_write_doubles_swe():
    """
    Reads from word3.txt word by word and inserts them in a svenska.bintree()
    If a word already exists as a value of a node, prints that word.
    :return:
    """
    print("\n")                                             # because looks matter
    with open("word3.txt", "r", encoding="utf-8") as svenskfil:
        for rad in svenskfil:
            ordet = rad.strip()
            if ordet in svenska:
                pass
            else:
                svenska.put(ordet)
    print("\n")


def check_path():
    """
    Takes user input for startord and slutord.
    Creates a node with startord as value and enqueues that node to q.
    While that queue is not empty, pops a node from q and calls makechildren()
    :return:
    """
    startord = input('Välj startord: ')
    slutord = input('Välj slutord: ')
    first_parent = ParentNode(startord)
    q.enqueue(first_parent)
    while not q.isEmpty():
        nod = q.dequeue()
        makechildren(nod, nod.value, slutord)
    if slutord not in gamla:
        print("Det finns ingen väg till", slutord)


def makechildren(startord, parent, slutord):
    """
    This function systematically loops thru all the different ways of changing
    one letter (using the swedish alphabet) in startordet. (aöt, böt, ..., söö)
    Checks if the newly created word exists in the bt svenska and if the word is not
    in bt gamla, if true - prints the words and adds in bt gamla.
    :param startord:
    :return:
    """
    alphabet = 'abcdefghijklmnopqrstuvwxyzåäö'
    counter = 0
    word = str(startord[:])
    ord_list = list(word)
    for char in word:
        for c in alphabet:
            ord_list[counter] = c
            new_word = "".join(ord_list)
            if new_word == slutord:
                parent_node = ParentNode(new_word, parent)
                writechain(parent_node)
                sys.exit()
            elif new_word in svenska and new_word not in gamla and new_word != word:
                parent_node = ParentNode(new_word, parent)
                q.enqueue(parent_node)
                gamla.put(new_word)
        ord_list = list(word)
        counter += 1


def writechain(child):
    """
    Recursive function for printing each parent starting with the parent at the highest level.
    :param child:
    :return:
    """
    if child.parent is None:
        print(child.value)
    elif child.parent is not None:
        writechain(child.parent)
        print(child.value)



q = LinkedQ()
svenska = Bintree()
gamla = Bintree()
read_write_doubles_swe()
check_path()

