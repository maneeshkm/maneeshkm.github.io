import unittest
from linear_regression import linear_regression
from pandas import DataFrame
import numpy as np
from pandas.util.testing import assert_frame_equal
from scipy.stats.stats import pearsonr


class TestLinearRegression(unittest.TestCase):
    """ Testing Linear Regression """

    def setUp(self):
        pass

    def test_linear_regression(self):
        X_test = DataFrame([1.5, 2.5, 3.5])
        y_test = DataFrame([1.5, 2.5, 3.5])

        fit = linear_regression(X_test, y_test)
        assert_frame_equal(y_test, DataFrame(fit.predict(X_test)))
        self.assertEqual(round(fit.coef_, 2), 1.0)
        self.assertEqual(round(fit.intercept_, 2), 0.0)
        r, _ = pearsonr(X_test.values, y_test.values)
        self.assertEqual(r, 1.0)


if __name__ == '__main__':
    unittest.main()
