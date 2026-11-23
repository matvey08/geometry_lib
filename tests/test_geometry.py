import ctypes
import unittest

geometry = ctypes.CDLL("./tests/libgeometry_test.dylib")
geometry.square_area.argtypes = [ctypes.c_double]
geometry.square_area.restype = ctypes.c_double


class GeometryTest(unittest.TestCase):
    def test_square_area(self):
        actual = geometry.square_area(3.0)
        self.assertEqual(actual, 10.0)