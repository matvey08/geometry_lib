import ctypes
import unittest

geometry = ctypes.CDLL("./tests/libgeometry_test.dylib")

geometry.square_area.argtypes = [ctypes.c_double]
geometry.square_area.restype = ctypes.c_double

geometry.square_perimeter.argtypes = [ctypes.c_double]
geometry.square_perimeter.restype = ctypes.c_double

geometry.rectangle_area.argtypes = [ctypes.c_double, ctypes.c_double]
geometry.rectangle_area.restype = ctypes.c_double

geometry.rectangle_perimeter.argtypes = [ctypes.c_double, ctypes.c_double]
geometry.rectangle_perimeter.restype = ctypes.c_double


class GeometryTest(unittest.TestCase):
    def test_square_area(self):
      res = geometry.square_area(3.0)
      self.assertEqual(res, 9.0)
    def test_square_area_zero(self):
      res = geometry.square_area(0.0)
      self.assertEqual(res, 0.0)
    def test_square_area_fraction(self):
      res = geometry.square_area(0.1)
      self.assertAlmostEqual(res, 0.01, places = 7)

    def test_square_perimeter(self):
      res = geometry.square_perimeter(3.0)
      self.assertEqual(res, 12.0)
    def test_square_perimeter_zero(self):
      res = geometry.square_perimeter(0.0)
      self.assertEqual(res, 0.0)
    def test_square_perimeter_fraction(self):
      res = geometry.square_perimeter(0.1)
      self.assertAlmostEqual(res, 0.4, places = 7)

    def test_rectangle_area(self):
      res = geometry.rectangle_area(3.0, 4.0)
      self.assertEqual(res, 12.0)
    def test_rectangle_area_zero_length(self):
      res = geometry.rectangle_area(0.0, 4.0)
      self.assertEqual(res, 0.0)
    def test_rectangle_area_zero_width(self):
      res = geometry.rectangle_area(3.0, 0.0)
      self.assertEqual(res, 0.0)
    def test_rectangle_area_fraction(self):
      res = geometry.rectangle_area(0.1, 0.2)
      self.assertAlmostEqual(res, 0.02, places = 7)
  
    def test_rectangle_perimeter(self):
      res = geometry.rectangle_perimeter(3.0, 4.0)
      self.assertEqual(res, 14.0)
    def test_rectangle_perimeter_zero(self):
      res = geometry.rectangle_perimeter(3.0, 0.0)
      self.assertEqual(res, 6.0)
    def test_rectangle_perimeter_fraction(self):
      res = geometry.rectangle_perimeter(0.1, 0.2)
      self.assertAlmostEqual(res, 0.6, places = 7)

      

