import unittest
from Lezione_9_Unitest import symmetric

class Testreenode(unittest.TestCase):
    def test_tree(self):
        listavuota = []
        with open("test1.txt",'r') as reader:
            for line in reader.readlines():
                listavuota.append(int(line.strip()))
        self.assertEqual(symmetric(listavuota), True)

            
if __name__ == "__main__":
    unittest.main()


