double SquareArea(double side);

double SquarePerimeter(double side);

double RectangleArea(double lenght, double width);

double RectanglePerimeter(double length, double width);

extern "C" double square_area(double side) { return SquareArea(side); }

extern "C" double square_perimeter(double side) {
  return SquarePerimeter(side);
}

extern "C" double rectangle_area(double length, double width) {
  return RectangleArea(length, width);
}

extern "C" double rectangle_perimeter(double length, double width) {
  return RectanglePerimeter(length, width);
}