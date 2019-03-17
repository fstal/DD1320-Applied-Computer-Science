import unittest
from main import wordToQ
from LinkedQ import LinkedQ, Syntaxfel

class Tests(unittest.TestCase):

    def testCorrect(self):
        mol_list = ['Cr2', 'Ka2453Re', 'Fr23L', 'Ck1', 'Ty']
        for mol in mol_list:
            mol_queue = LinkedQ()
            self.assertTrue(wordToQ(mol_queue, mol), msg=("Somthing is wrong"))

    def testError(self):
        mol_list = ['Cr0', 'Crsdfsd', 'C0', 'Tyy']
        for mol in mol_list:
            mol_queue = LinkedQ()
            with self.assertRaises(Syntaxfel, msg=("Somthing is wrong")):
                wordToQ(mol_queue, mol)



