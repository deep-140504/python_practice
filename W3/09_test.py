import unittest

def is_sorted(lst):
    return all(lst[i] <= lst[i + 1] for i in range (len(lst) - 1))
class TestSortedAscending(unittest.TestCase):
    def test_sorted(self):
        lst = [1, 2, 3, 4, 5]
        self.assertTrue(is_sorted(lst), "This is not sorted in ascending order")
    def test_unsorted(self):
        lst = [1, 5, 2, 3, 4]
        self.assertFalse(is_sorted(lst), "This is sorted in ascending order")

if __name__ == "__main__":
    unittest.main()