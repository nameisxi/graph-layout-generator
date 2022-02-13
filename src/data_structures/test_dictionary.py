import unittest

from dictionary import Dictionary


class TestDictionary(unittest.TestCase):
    def test_dictionary_size(self):
        d = Dictionary({})
        self.assertEqual(d.size, 0)

        d = Dictionary({
            'root': {},
            'child_1': {},
            'child_2': {},
            'child_3': {}
        })
        self.assertEqual(d.size, 4)
        