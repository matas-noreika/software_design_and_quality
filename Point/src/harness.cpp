/*
 * Programmer: Matas Noreika 2025-11-10 11:03
 * Purpose: Test harness for point class
*/

#include <iostream>
#include "Point.h"
#define MY_PI acos(-1)

int main(){

  Point p1(3.0, 5.0);

  p1.print_xy(); std::cout << " : "; p1.print_rtheata(); std::cout << '\n';

  p1.translate(-1,1);

  p1.print_xy(); std::cout << " : "; p1.print_rtheata(); std::cout << '\n';
  
  return 0;
}
