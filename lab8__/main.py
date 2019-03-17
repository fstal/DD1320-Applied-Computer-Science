from LinkedQ import LinkedQ
from LinkedQ import Syntaxfel


def wordToQ(mol_queue, mol):
    #mol = input('Skriv molekyl: ')
    mol_length = len(mol)
    for char in mol:
        mol_queue.enqueue(char)
    return molCheck(mol_queue, mol_length)


def molCheck(mol_queue, mol_length):
    for i in range(mol_length):
        value_pair = mol_queue.getValuePair()
        current_value = value_pair[0]
        peek_value = value_pair[1]
        if peek_value in upper_case_alpha:
            capLetter(current_value)
        elif peek_value in lower_case_alpha:
            lowLetter(current_value)
        elif peek_value in numbers_x:
            numbersX(current_value)
        elif peek_value == '0':
            isZero(current_value)
        elif peek_value is None:
            isNone(current_value)
    print('Formeln är syntastikst korrekt')
    return True


def capLetter(current_value):
    if current_value in upper_case_alpha or current_value in lower_case_alpha or int(current_value) in numbers_y:
        return True
    else:
        raise Syntaxfel("capLetter ger fel för current value: ", current_value)


def lowLetter(current_value):
    if current_value in upper_case_alpha:
        return True
    else:
        raise Syntaxfel("lowLetter ger fel för current value: ", current_value)


def numbersX(current_value):
    if current_value in upper_case_alpha or current_value in lower_case_alpha or int(current_value) in numbers_y:
        return True
    else:
        raise Syntaxfel("numbersX ger fel för current value: ", current_value)


def isZero(current_value):
    #print(current_value)
    if current_value in numbers_y:
        return True
    else:
        raise Syntaxfel("isZero ger fel för current value: ", current_value)


def isNone(current_value):
    if current_value in upper_case_alpha or current_value in lower_case_alpha or current_value in numbers_y:
        return True
    else:
        raise Syntaxfel("isNone ger fel för current value: ", current_value)


numbers_x = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
numbers_y = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

#numbers_y = list(range(0, 10))
#numbers_x = list(range(1, 10))
lower_case_alpha = []
blaj = ['H2', 'cr12', 'Cr0', 'Pb1', 'Mn4', 'CaN012']
upper_case_alpha = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
             'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

for bokstav in upper_case_alpha:
    lower_case_alpha.append(bokstav.lower())
    
mol_queue = LinkedQ()
#
wordToQ(mol_queue, 'Cr2')