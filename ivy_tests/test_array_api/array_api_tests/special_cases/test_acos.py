"""
Special cases tests for acos.

These tests are generated from the special cases listed in the spec.

NOTE: This file is generated automatically by the generate_stubs.py script. Do
not modify it directly.
"""

from ..array_helpers import NaN, assert_exactly_equal, exactly_equal, greater, less, one, zero
from ..hypothesis_helpers import numeric_arrays
from .._array_module import acos

from hypothesis import given

#
# @given(numeric_arrays)
# def test_acos_special_cases_one_arg_equal_1(arg1):
#     """
#     Special case test for `acos(x, /)`:
#
#         -   If `x_i` is `NaN`, the result is `NaN`.
#
#     """
#     res = acos(arg1)
#     mask = exactly_equal(arg1, NaN(arg1.shape, arg1.dtype))
#     assert_exactly_equal(res[mask], (NaN(arg1.shape, arg1.dtype))[mask])
#
#
# @given(numeric_arrays)
# def test_acos_special_cases_one_arg_equal_2(arg1):
#     """
#     Special case test for `acos(x, /)`:
#
#         -   If `x_i` is `1`, the result is `+0`.
#
#     """
#     res = acos(arg1)
#     mask = exactly_equal(arg1, one(arg1.shape, arg1.dtype))
#     assert_exactly_equal(res[mask], (zero(arg1.shape, arg1.dtype))[mask])
#
#
# @given(numeric_arrays)
# def test_acos_special_cases_one_arg_greater(arg1):
#     """
#     Special case test for `acos(x, /)`:
#
#         -   If `x_i` is greater than `1`, the result is `NaN`.
#
#     """
#     res = acos(arg1)
#     mask = greater(arg1, one(arg1.shape, arg1.dtype))
#     assert_exactly_equal(res[mask], (NaN(arg1.shape, arg1.dtype))[mask])
#
#
# @given(numeric_arrays)
# def test_acos_special_cases_one_arg_less(arg1):
#     """
#     Special case test for `acos(x, /)`:
#
#         -   If `x_i` is less than `-1`, the result is `NaN`.
#
#     """
#     res = acos(arg1)
#     mask = less(arg1, -one(arg1.shape, arg1.dtype))
#     assert_exactly_equal(res[mask], (NaN(arg1.shape, arg1.dtype))[mask])
