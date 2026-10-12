#include <iostream>

// Вычисляет площадь квадрата
double SquareArea(double side);

// Вычисляет периметр квадрата 
double SquarePerimeter(double side);

// Вычисляет площадь прямоугольника.
double RectangleArea(double length, double width);

// Вычисляет периметр прямоугольника.
double RectanglePerimeter(double length, double width);

int main() {

    double side = 4.0;
    std::cout << "Площадь квадрата: " << SquareArea(side) << std::endl;
    std::cout << "Перимтер квадрата: " << SquarePerimeter(side) << std::endl;

    double length = 3.0, width = 5.0;
    std::cout << "Площадь прямоугольника: " << RectangleArea(length, width) << std::endl;
    std::cout << "Периметр прямоугольника: " << RectanglePerimeter(length, width) << std::endl;

    return 0;
}