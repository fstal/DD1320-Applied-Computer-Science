from bintreeFile import Bintree
from linkedQFile import LinkedQ
from bintreeFile import Node
from string import ascii_lowercase


def read_write_doubles_swe():
    """
    Reads from word3.txt word by word and inserts them in a svenska.bintree()
    If a word already exists as a value of a node, does nothing.
    :return:
    """
    print("\n")                                                          #because looks matter
    with open("word3.txt", "r", encoding="utf-8") as svenskfil:
        for rad in svenskfil:
            ordet = rad.strip()
            if ordet in svenska:
                pass
                #print(ordet, end=" ")
            else:
                svenska.put(ordet)
    print("\n")
    startord = input('Välj startord: ')
    #slutord = input('Välj slutord: ')
    makechildren(startord)

def test_function():
    """
    Function used in testing

    """

    print("\n")                                #because looks matter
    with open("word3.txt", "r", encoding="utf-8") as svenskfil:
        kattmat = 0
        for rad in svenskfil:
            if kattmat <= 9:
                ordet = rad.strip()
                if ordet in svenska:
                    pass
                    #print(ordet, end=" ")
                else:
                    svenska.put(ordet)
                    print(ordet)
            kattmat += 1
    print("\n")
    #svenska.write_inorder()
    nod = ''
    startord = input('Välj startord: ')
    makechildren(startord)
    #slutord = input('Välj slutord: ')
    #q.enqueue(startord)



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
    ordet = startord[:]  # bort?
    ord_list = list(startord)   # immutable shiss
    for char in ordet:
        for letter in alphabet:
            ord_list[counter] = letter
            if "".join(ord_list) in svenska and "".join(ord_list) not in gamla and "".join(ord_list) != ordet:
                print("".join(ord_list))
                gamla.put("".join(ord_list))
        ord_list = list(ordet)      # startord
        counter += 1


q = LinkedQ()
svenska = Bintree()
gamla = Bintree()
read_write_doubles_swe()
