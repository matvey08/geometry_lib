import ctypes
import unittest

geometry = ctypes.CDLL("./tests/libgeometry_test.dylib")

geometry.square_area.argtypes = [ctypes.c_double]
geometry.square_area.restype = ctypes.c_double

geometry.square_perimeter.argtypes = [ctypes.c_double]
geometry.square_perimeter.restype = ctypes.c_double


class GeometryTest(unittest.TestCase):
    def test_square_area(self):
        actual = geometry.square_area(3.0)
        self.assertEqual(actual, 9.0)
    def test_square_area_zero(self):
      actual = geometry.square_area(0.0)
      self.assertEqual(actual, 0.0)
    def test_square_area_fraction(self):
      actual = geometry.square_area(0.1)
      self.assertAlmostEqual(actual, 0.01, places = 7)

    def test_square_perimeter(self):
      actual = geometry.square_perimeter(3.0)
      self.assertEqual(actual, 12.0)
    def test_square_perimeter_zero(self):
      actual = geometry.square_perimeter(0.0)
      self.assertEqual(actual, 0.0)
    def test_square_perimeter_fraction(self):
      actual = geometry.square_perimeter(0.1)
      self.assertEqual(actual, 0.4)

