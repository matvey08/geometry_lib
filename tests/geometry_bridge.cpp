double SquareArea(double side);

extern "C" double square_area(double side) { return SquareArea(side); }