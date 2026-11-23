double SquareArea(double side);

double SquarePerimeter(double side);

extern "C" double square_area(double side) { return SquareArea(side); }

extern "C" double square_perimeter(double side) {
  return SquarePerimeter(side);
}