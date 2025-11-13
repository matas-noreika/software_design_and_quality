/*
 * Programmer: Matas Noreika 2025-11-10 11:06
 * Purpose: Class definition of Point
*/

#ifndef __POINT_H__
#define __POINT_H__

#include <iostream>
#include <cmath>

class Point {
  double x,y;
  public:

  //constructor
  Point(double xx = 0, double yy = 0): x(xx), y(yy){
  }
  //distance method
  double distance(){
    double x_sqr = x*x;
    double y_sqr = y*y;
    return sqrt(x_sqr + y_sqr);
  }
  void translate(double xx, double yy){
    x += xx;
    y += yy;
  }
  double angle(){
    return atan2(y,x);
  }

  void print_xy(){
    std::cout << "x : " << x << ", y : " << y;
  }

  void print_rtheata(){
    std::cout << "r : " << distance() << ", theata : " << angle();
  }
};
#endif
