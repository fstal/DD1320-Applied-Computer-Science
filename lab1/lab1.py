import time
import csv

class Pokemon:
    """
    A class for each pokemon.
    Arrtibutes: name, type1, type2, tier and ability1 which all corresponds to the values in the csv-file
    """
    def __init__(self, name, type1, type2, tier, ability1):
        self.name = name
        self.type1 = type1
        self.type2 = type2
        self.tier = tier
        self.ability1 = ability1

    def __str__(self):
        """
        Method which returns the attributes of a pokemon
        """
        string = 'Your Pokemon has the following attributes: %s, %s, %s, %s, %s' % (self.name, self.type1, self.type2, self.tier, self.ability1)
        return string

    def change_name(self):
        """
        Method which changes the "name" attribute of a pokemon
        """
        input_name = input('Change name to: ')
        self.name = input_name
        print('Your new name is: ' + self.name)

    def change_tier(self):
        """
        Method which changes the "tier" attribute of a pokemon
        """
        input_tier = input('Change tier to: ')
        self.tier = input_tier

    def is_grass_type(self):
        """
        Method which checks if a pokemon is a grass-type or not
        """
        if self.type1 == 'Grass' or self.type2 == 'Grass':
            return 'This is a grass-type pokemon'
        else:
            return 'This is not a grass-type pokemon'

    def one_type_check(self):
        """
        Method which checks if a pokemon has more than one type
        """
        if self.type2 == '':
            print('The pokemon only has one type')
        else:
            print('The pokemon has type ' + self.type1 + ' and ' + self.type2)


def csv_to_list():
    """
    Compiles our CSV file in to a list
    """
    with open('Excel Pkdx V5.14 - Pokedex.csv', 'r') as read:
        reader = csv.reader(read)
        pokemon_list = list(reader)
    object_creator(pokemon_list)


def object_creator(pokemon_list):
    """
    Function which creates an object for each pokemon in our list
    """
    for i in pokemon_list:
        if i == pokemon_list[0]:
            pass
        else:
            created_pokemon = Pokemon(i[2], i[10], i[11], i[12], i[13])
            object_list.append(created_pokemon)

def search_pokemon():
    """
    Function used to search through the names of the pokemon in our list of pokemon objects
    """
    search_name = input('Enter a name: ')

    for obj in object_list:
        if search_name == obj.name:
            return(obj)
        else:
            pass


def menu():
    """
    A menu which let's the user decide what he/she want's to do.
    Each choice corresponds to a different method in our class.
    """
    choice = input('1. Search, 2. Change name, 3. Change Tier, 4. Check if grass type, 5. Check type')
    choice = int(choice)
    if choice == 1:
        print(search_pokemon())
    elif choice == 2:
        search_pokemon().change_name()
    elif choice == 3:
        search_pokemon().change_tier()
    elif choice == 4:
        print(search_pokemon().is_grass_type())
    elif choice == 5:
        search_pokemon().one_type_check()
    else:
         print('Nope')




object_list = []
csv_to_list()
menu()
