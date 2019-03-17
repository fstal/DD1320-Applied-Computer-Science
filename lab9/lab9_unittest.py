import unittest
from lab9_redovisning import LinkedQ, Syntaxfel, start

class Tests(unittest.TestCase):

    def testSample1(self):
        start('Na')
        start('H2O')
        start('Si(C3(COOH)2)4(H2O)7')
        start('Na332')
        self.assert_(True)

    def testSample2(self):
        mol_list = ['Cr0', 'C(OH4)C', 'C(OH4C', 'H2O)Fe', 'H0', 'H1C', 'H02C', 'Nacl', 'a', '(Cl)2)3', ')', '2']
        #mol_list = ['Cr0']
        for mol in mol_list:
            with self.assertRaises(Syntaxfel, msg=("Somthing is wrong")):
                start(mol)