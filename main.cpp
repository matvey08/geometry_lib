#include <iostream>

// Вычисляет площадь квадрата
double SquareArea(double side);

int main() {

    double side = 4.0;
    std::cout << "Площадь квадрата: " << SquareArea(side) << std::endl;

    return 0;
}