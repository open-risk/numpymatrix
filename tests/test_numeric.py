import numpy as np
from numpy.testing import assert_equal

import numpymatrix as npm


class TestDot:
    def test_matscalar(self):
        b1 = npm.matrix(np.ones((3, 3), dtype=complex))
        assert_equal(b1 * 1.0, b1)


def test_diagonal():
    b1 = npm.matrix([[1, 2], [3, 4]])

    diag_b1 = npm.matrix([[1, 4]])
    array_b1 = np.array([1, 4])

    assert_equal(b1.diagonal(), diag_b1)
    assert_equal(np.diagonal(b1), array_b1)
    assert_equal(np.diag(b1), array_b1)
