import numpy as np
from numpy.compat import asbytes
from numpy.testing import *
import sys, warnings

# The C implementation of fancy indexing is relatively complicated,
# and has many seeming inconsistencies. It also appears to lack any
# kind of test suite, making any changes to the underlying code difficult
# because of its fragility.

# This file is to remedy the test suite part a little bit,
# but hopefully NumPy indexing can be changed to be more systematic
# at some point in the future.

def test_boolean_indexing():
    # Indexing a 2-dimensional array with a length-1 array of 'True'
    a = np.array([[ 0.,  0.,  0.]])
    b = np.array([ True], dtype=bool)
    assert_equal(a[b], a)

    a[b] = 1.
    assert_equal(a, [[1., 1., 1.]])


def test_boolean_assignment_value_mismatch():
    # A boolean assignment should fail when the shape of the values
    # cannot be broadcasted to the subscription. (see also gh-3458)
    a = np.arange(4)
    def f(a, v):
        a[a > -1] = v

    assert_raises(ValueError, f, a, [])
    assert_raises(ValueError, f, a, [1, 2, 3])
    assert_raises(ValueError, f, a[:1], [1, 2, 3])


if __name__ == "__main__":
    run_module_suite()
