import unittest
from mdict import *


class TestMdict(unittest.TestCase):
    def setUp(self):
        self.test_dict = {}

    def test_mget(self):
        """
        mget should get the correct value from the dict
        """
        self.test_dict['a'] = 1
        self.assertEqual(mget(self.test_dict, 'a'), 1)

    def test_mget_default(self):
        """
        mget should return the default value when the key is not found
        """
        val = mget(self.test_dict, 'fake:key:list', default="pass")
        self.assertEqual(val, "pass")

    def test_mget_default_None(self):
        """
        mget should return None when key is not found and no default is specified
        """
        val = mget(self.test_dict, 'fake:key:list')
        self.assertIsNone(val)

    def test_mset(self):
        """
        mset should set the correct value inside dict
        """
        mset(self.test_dict, 'b:c:d', 5)
        self.assertEqual(self.test_dict['b']['c']['d'], 5)

    def test_mset_multiple_times(self):
        """
        mset should set the correct value inside dict
        even when called multiple times on the same keys
        """
        mset(self.test_dict, 'b:c:d', 5)
        self.assertEqual(self.test_dict['b']['c']['d'], 5)

        mset(self.test_dict, 'b:c:d', 6)
        self.assertEqual(self.test_dict['b']['c']['d'], 6)

    def test_mset_delimiter(self):
        """
        mset should work with different delimiters
        """
        mset(self.test_dict, 'b,c,d', 6, delimiter=',')
        self.assertEqual(self.test_dict['b']['c']['d'], 6)

    def test_mset_None(self):
        """
        mset with None value should also work
        """
        mset(self.test_dict, 'a:b:none', None)
        self.assertIsNone(self.test_dict['a']['b']['none'])

if __name__ == "__main__":
    unittest.main()
