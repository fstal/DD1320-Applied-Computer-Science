"""

katt = [['ost', 'asd'], ['majs', 'gurka']]


for i in katt:
    if i == katt[0]:
        print('första rad')
    else:
        print(i)
        print(i[0])
    #i = i + 1

#print(katt[1])
"""
"""
def pokemon_maker():
    print('We will now proceed to create a Pokemon')
    time.sleep(2)
    name = input('Choose a name: ')
    type1 = input('Choose a type: ')
    type2 = input('Choose a second type OR leave the field empty: ')
    tier = input('Choose a tier: ')
    ability1 = input('Choose an ability; ')
    new_pokemon = Pokemon(name, type1, type2, tier, ability1)
    print(new_pokemon)
"""