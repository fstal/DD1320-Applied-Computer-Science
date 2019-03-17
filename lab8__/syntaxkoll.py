
def symbolkoll():
    """
    kollar vad för sorts tecken och gör shiss beroende på vad det är
    :return:
    """
    if molekyl[0] not in alfastora:
        print('katt')

    for tecken in molekyl:
        if tecken.isalpha():
            bokstavskoll(tecken)
        elif tecken.isnumeric():
            print(tecken.isnumeric())
            #sifferkoll(tecken)
        else:
            print('syntaxfel')


def bokstavskoll(tecken):
    if tecken in alfasmå or tecken in alfastora:
        return True
    else:
        return False

def sifferkoll(tecken):
    print('aksdfkas')





alfastora = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
             'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
alfasmå = []

for bokstav in alfastora:
    alfasmå.append(bokstav.lower())

print(alfasmå)
molekyl = ['HgO2']
