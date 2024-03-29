from bintreeFile import Bintree
from linkedQFile import LinkedQ
from bintreeFile import Node
from string import ascii_lowercase


def read_write_doubles_swe():
    """
    Reads from word3.txt word by word and inserts them in a svenska.bintree()
    If a word already exists as a value of a node, prints that word.
    :return:
    """
    print("\n")                                             #because looks matter
    with open("word3.txt", "r", encoding="utf-8") as svenskfil:
        for rad in svenskfil:
            ordet = rad.strip()
            if ordet in svenska:
                pass
            else:
                svenska.put(ordet)
    print("\n")

def check_path():
    nod = ''
    startord = input('Välj startord: ')
    slutord = input('Välj slutord: ')
    q.enqueue(startord)
    while not q.isEmpty():
        nod = q.dequeue()
        if slutord in gamla:
            print("Det finns en väg till ", slutord)
            break
        else:
            makechildren(nod)
    if slutord not in gamla:
        print("Det finns ingen väg till", slutord)


def makechildren(startord):
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
    ordet = str(startord[:])
    ord_list = list(ordet)
    for char in ordet:
        for c in alphabet:
            ord_list[counter] = c
            if "".join(ord_list) in svenska and "".join(ord_list) not in gamla and "".join(ord_list) != ordet:
                q.enqueue("".join(ord_list))
                gamla.put("".join(ord_list))
        ord_list = list(ordet)
        counter = counter + 1


q = LinkedQ()
svenska = Bintree()
gamla = Bintree()
read_write_doubles_swe()
check_path()

