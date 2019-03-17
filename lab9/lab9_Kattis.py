import sys
"""
Filip Stål
Joel Weidenmark
"""


class LinkedQ:
    """
    Class for our queue of nodes. Contains two private attributes which refrences to the first and last node in the queue
    """

    def __init__(self):
        self.__firstnode = None
        self.__lastnode = None
        self.__activenode = self.__firstnode

    def enqueue(self, x):
        """
        Creates a new node and places it last in the queue.
        If it's the only node in the queue it is also saved to __firstnode
        x = the value of the node
        """
        newNode = Node(x)
        newNode.next = None  # The last node in a queue doesn't have any "next"
        if self.__firstnode is None:  # If there is no __firstnode our newNode becomes __firstnode
            self.__firstnode = newNode
            self.__activenode = self.__firstnode
            self.__lastnode = newNode

        else:  # If there already is a __firstnode our newNode is the last node in the queue
            self.__lastnode.next = newNode  # Gives the previous __lastnode a __lastnode.next
            self.__lastnode = newNode  # Sets the new __lastnode to newNode

    def getValuePair(self):
        """
        Metod used for Lab8, returns a list with two elements
        The first being our current_value and the second
        being the next - or the the so called peek_value
        :return:
        """
        value_pair = [self.__activenode.value, self.peek()]
        self.__activenode = self.__activenode.next
        return value_pair

    def peek(self):
        """
        peek() the way we figured it should be used in Lab9. Returns None
        if self activenode is actually None (circumventing the NoneType error thingie)
        :return:
        """
        if self.__activenode is not None:
            return self.__activenode.value
        else:
            return None

    def dequeue(self):
        """
        Removes the first node in the queue
        Returns the value of the first node
        """
        temp = self.__firstnode  # Saves the value of the __firstnode before we change the first node
        self.__firstnode = self.__firstnode.next  # sets the first node equal to the next node
        self.__activenode = self.__firstnode
        return str(temp)

    def isEmpty(self):
        """
        Checks if the queue is empty by checking if there is a __firstnode
        Returns True if empty and False otherwise
        """
        return self.__firstnode is None

    def __str__(self):
        if self.isEmpty():
            return ''
        else:
            self.__activenode = self.__firstnode
            remaining_q = str(self.__activenode.value)
            while self.__activenode is not self.__lastnode:
                remaining_q = remaining_q + str(self.__activenode.next.value)
                self.__activenode = self.__activenode.next
            self.__activenode = self.__firstnode
        return remaining_q


class Node:
    """
    Class for each Node which contains the nodes value and a reference to the node next to it
    """

    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next

    def __str__(self):
        """
        Returns the value of the node
        """
        return str(self.value)


class Syntaxfel(Exception):
    """
    Inherits from Exception. We raise this when something isnt correct according to syntax
    raised with a print describing the error
    Eg. 'Saknad stor bokstav', 'För litet tal vid radslutet'
    """
    pass


def start():
    kattis = []
    """
    try:
        queueCreator('((Na)2Cl)3')
    except Syntaxfel as msg:
        print(msg)
    with open('sample_input2.txt', 'r') as read:
        for row in read:
            row.strip('\n')
            if '#' in row:
                break
            else:
                kattis.append(row.strip('\n'))
        for element in kattis:
            try:
                queueCreator(element)
            except Syntaxfel as msg:
                print(msg)
    """
    for row in sys.stdin:
        row.strip('\n')
        if '#' in row:
            break
        else:
            kattis.append(row.strip('\n'))
    for element in kattis:
        if len(stack) > 0:
            for k in range(len(stack)):
                stack.pop()
        try:
            queueCreator(element)
        except Syntaxfel as msg:
            print(msg)


def queueCreator(element):
    mol_q = LinkedQ()
    for char in element:
        mol_q.enqueue(char)
    molCheck(mol_q)


def molCheck(mol_q):
    if not mol_q.isEmpty():
        if mol_q.peek() is ')':
            try:
                stack.pop()
                mol_q.dequeue()
            except:
                raise Syntaxfel('Felaktig gruppstart vid radslutet ' + str(mol_q))
            numCheck(mol_q)
            molCheck(mol_q)
            return
        else:
            alphaCheck(mol_q)
            molCheck(mol_q)
    else:
        if len(stack) > 0:
            for k in range(len(stack)):
                stack.pop()
            raise Syntaxfel('Saknad högerparentes vid radslutet' + str(mol_q))
        else:
            print('Formeln är syntaktiskt korrekt')

"""
def paraCheck(mol_q):
    if not mol_q.isEmpty():
        if mol_q.peek() is ')':
            try:
                stack.pop()
                mol_q.dequeue()
            except:
                raise Syntaxfel('Felaktig gruppstart vid radslutet ' + str(mol_q))
        else:
            alphaCheck(mol_q)
            paraCheck(mol_q)
"""


def alphaCheck(mol_q):
    """
    Checks for uppercase alphabetical chars and lowercase alphabetical chars
    Validates these with the list och acceptable atoms (single or double letter combinations)
    Semi-checks parantheses as well
           # Handle parentheses (stavning lol?) with stack...?
           if mol_q.peek() is ')':
               try:
                   stack.pop()
                   mol_q.dequeue()
               except:
                   raise Syntaxfel('Felaktig gruppstart vid radslutet' + str(mol_q))
   """
    if not mol_q.isEmpty():
        if mol_q.peek() in lower_case_alpha:
            raise Syntaxfel('Saknad stor bokstav vid radslutet ' + str(mol_q))

        elif mol_q.peek() is '(':
            stack.append(mol_q.peek())
            mol_q.dequeue()

            if mol_q.peek() is ')':
                raise Syntaxfel('Felaktig gruppstart vid radslutet ' + str(mol_q))
            else:
                return

        elif mol_q.peek() is ')':
            try:
                stack.pop()
                mol_q.dequeue()
                numCheck(mol_q)
            except:
                raise Syntaxfel('Felaktig gruppstart vid radslutet ' + str(mol_q))

            if mol_q.peek() in numbers:
                numCheck(mol_q)
                return
            else:
                raise Syntaxfel('Saknad siffra vid radslutet ' + str(mol_q))

        elif mol_q.peek() in upper_case_alpha:
            atomCheck(mol_q)
            if mol_q.peek() in numbers:
                numCheck(mol_q)
                return
            return

        else:
            raise Syntaxfel('Felaktig gruppstart vid radslutet ' + str(mol_q))


def atomCheck(mol_q):
    """
    When an alphabetical upper-case-char i encountered we check if its a valid atom
    :param mol_q:
    :return:
    """
    if not mol_q.isEmpty():
        letter = mol_q.dequeue()
        if mol_q.peek() in lower_case_alpha:
            atom = letter + mol_q.dequeue()
            if atom in atom_list:
                return
            else:
                raise Syntaxfel('Okänd atom vid radslutet ' + str(mol_q))
        else:
            if letter in atom_list:
                return
            else:
                raise Syntaxfel('Okänd atom vid radslutet ' + str(mol_q))


def numCheck(mol_q):
    if not mol_q.isEmpty():
        if mol_q.peek() in numbers:
            number = mol_q.dequeue()
            if number == '0':
                raise Syntaxfel('För litet tal vid radslutet ' + str(mol_q))
            else:
                while mol_q.peek() in numbers:
                    number = number + mol_q.dequeue()
                if number == '1':
                    raise Syntaxfel('För litet tal vid radslutet ' + str(mol_q))
                else:
                    return
        else:
            raise Syntaxfel('Saknad siffra vid radslutet ' + str(mol_q))
    else:
        raise Syntaxfel('Saknad siffra vid radslutet ' + str(mol_q))

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
upper_case_alpha = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
                    'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
lower_case_alpha = []
for i in upper_case_alpha:
    lower_case_alpha.append(i.lower())

stack = []

atom_list = ['H', 'He', 'Li', 'Be', 'B', 'C', 'N', 'O', 'F', 'Ne', 'Na', 'Mg', 'Al', 'Si', 'P', 'S', 'Cl', 'Ar',
             'K', 'Ca', 'Sc', 'Ti', 'V', 'Cr', 'Mn', 'Fe', 'Co', 'Ni', 'Cu', 'Zn', 'Ga', 'Ge', 'As', 'Se', 'Br',
             'Kr', 'Rb', 'Sr', 'Y', 'Zr', 'Nb', 'Mo', 'Tc', 'Ru', 'Rh', 'Pd', 'Ag', 'Cd', 'In', 'Sn', 'Sb', 'Te',
             'I', 'Xe', 'Cs', 'Ba', 'La', 'Ce', 'Pr', 'Nd', 'Pm', 'Sm', 'Eu', 'Gd', 'Tb', 'Dy', 'Ho', 'Er', 'Tm',
             'Yb', 'Lu', 'Hf', 'Ta', 'W', 'Re', 'Os', 'Ir', 'Pt', 'Au', 'Hg', 'Tl', 'Pb', 'Bi', 'Po', 'At', 'Rn',
             'Fr', 'Ra', 'Ac', 'Th', 'Pa', 'U', 'Np', 'Pu', 'Am', 'Cm', 'Bk', 'Cf', 'Es', 'Fm', 'Md', 'No', 'Lr',
             'Rf', 'Db', 'Sg', 'Bh', 'Hs', 'Mt', 'Ds', 'Rg', 'Cn', 'Fl', 'Lv']

start()