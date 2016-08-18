import unittest

from my_sum import my_sum

class MySumTests(unittest.TestCase):

    def setUp(self):
        self.numbers = [10, 5, 7, 8, 90, 60]
    
    def test_sum_of_numbers(self):
        '''
        Test sum of numbers
        '''

        self.assertEqual(my_sum(10, 5), 15)
        self.assertEqual(my_sum(5, 7), 12)
        self.assertEqual(my_sum(8, 90), 98)
        self.assertEqual(my_sum(60, 90), 150)
        self.assertEqual(my_sum(60, 8), 68)
        self.assertEqual(my_sum(60, 10), 70)
        self.assertEqual(my_sum(60, 5), 65)

    def test_non_numbers(self):
        self.assertEqual(my_sum('10', '4'), "Invalid input")
        self.assertEqual(my_sum('2', 4), "Invalid input")
        self.assertEqual(my_sum(2, '4'), "Invalid input")

if __name__ == '__main__':
    unittest.main()
