from bintreeFile import Bintree
from bintreeFile import Node


def read_write_doubles_swe():
    """
    Reads from word3.txt word by word and inserts them in a svenska.bintree()
    If a word already exists as a value of a node, prints that word.
    :return:
    """
    print("\n")                                #because looks matter
    with open("word3.txt", "r", encoding="utf-8") as svenskfil:
        for rad in svenskfil:
            ordet = rad.strip()
            if ordet in svenska:
                print(ordet, end=" ")
            else:
                svenska.put(ordet)
    print("\n")


def read_write_katt_eng():
    """
    Reads from engelska.txt row by row, splits the row into a list of strings,
    with each word representing an element in the list.
    Loops through the elements of the list, if an element already exists as a value of a node in engelska.bintree,
    does nothing.
    Else, checks if elements exists in svenska.bintree, if True, prints that word.
    :return:
    """
    with open("engelska.txt", "r", encoding="utf-8") as engelskfil:
        for row in engelskfil:
            words = row.split()
            for element in words:
                for char in ['"', ',', '.', "'"]:
                    element = element.replace(char, '')
                if str(element) in engelska:
                    pass
                else:
                    if str(element) in svenska:
                        print(element, end=" ")
                engelska.put(element)
    print("\n")

engelska = Bintree()
svenska = Bintree()

read_write_doubles_swe()
read_write_katt_eng()
engelska.write_inorder()
