import a1
import unittest


class TestStockPriceSummary(unittest.TestCase):
    """ Test class for function a1.stock_price_summary. """

    # Add your test methods for a1.stock_price_summary here.
    def test_stock_price_summary_1(self):
        """Test stock_price_summary with [0.01, 0.03, -0.02, -0.14, 0, 0, 0.10, -0.01]"""
        actual = a1.stock_price_summary([0.01, 0.03, -0.02, -0.14, 0, 0, 0.10, -0.01])
        expected = (0.14, -0.17)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main(exit=False)
