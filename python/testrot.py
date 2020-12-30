import unittest

from rotN import rotN

class Test(unittest.TestCase):

    def test_rotN(self):
        Ntest = 13
        chatest = "abcvwxyz"
        expected = "nopijklm"
        actual = rotN(Ntest,chatest)
        self.assertEqual(expected,actual)

    def test_rotN2(self):
        Ntest = 2
        chatest = "abcvwxyz"
        expected = "cdexyzab"
        actual = rotN(Ntest,chatest)
        self.assertEqual(expected,actual)

    def test_rotN3(self):
        Ntest = 10
        chatest = "adofrubdp"
        expected = "knypbelnz"
        actual = rotN(Ntest,chatest)
        self.assertEqual(expected,actual)
        
if __name__ == "__main__":
    unittest.main()
