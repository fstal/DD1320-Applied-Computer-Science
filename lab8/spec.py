# Syntaxkontroll

from wordqueue import WordQueue
"""
Flergrenade definitioner kräver tjuvtitt medq.peek() som vi har lagt till i klassen WordQueue.
"""
class Grammatikfel(Exception):
    """
    Generar en print när något strider mot syntaxen som beskriver vad som var fel
    Ex. "Saknad stor bokstav", "För litet tal vid radslutet"

    """
    pass

def readMolekyl(q):
    """
    <molekyl> ::= <atom> | <atom><num>
    :param q:
    :return:
    """
    readAtom(q)
    if q.peek() == ".":
        q.dequeue()
    else:
        readKonj(q)
        readMolekyl(q)

def readAtom(q):
    """
    <atom>  ::= <LETTER> | <LETTER><letter>
    :param q:
    :return:
    """
    readSubj(q)
    readPred(q)

def readSubj(q):
    word = q.dequeue()
    if word == "JAG":
        return
    if word == "DU":
        return
    raise Grammatikfel("Fel subjekt: " + word)

def readPred(q):
    word = q.dequeue()
    if word == "TROR":
        return
    if word == "VET":
        return
    raise Grammatikfel("Fel predikat: " + word)

def readKonj(q):
    word = q.dequeue()
    if word == "ATT":
        return
    if word == "OCH":
        return
    raise Grammatikfel("Fel konjunktion: " + word)

def printQueue(q):
    while not q.isEmpty():
        word = q.dequeue()
        print(word, end = " ")
    print()

def storeSentence(Molekyl):
    q = WordQueue()
    Molekyl = Molekyl.split()
    for ordet in Molekyl:
        q.enqueue(ordet)
    q.enqueue(".")
    return q


def kollaGrammatiken(Molekyl):
    q = storeSentence(Molekyl)

    try:
        readMolekyl(q)
        return "Följer syntaxen!"
    except Grammatikfel as fel:
        return str(fel) + " före " + str(q)

def main():
    q = WordQueue()
    Molekyl = input("Skriv en Molekyl: ")
    resultat = kollaGrammatiken(Molekyl)
    print(resultat)

if __name__ == "__main__":
    main()

