import a1
import unittest


class TestSwapK(unittest.TestCase):
    """ Test class for function a1.swap_k. """

    # Add your test methods for a1.swap_k here.
    def test_swap_k_1(self):
        """Test swap_k with [1, 2, 3, 4, 5, 6] and 2"""

        nums = [1, 2, 3, 4, 5, 6]
        expected = [5, 6, 3, 4, 1, 2]
        a1.swap_k(nums, 2)
        self.assertEqual(expected, nums)


if __name__ == '__main__':
    unittest.main(exit=False)
