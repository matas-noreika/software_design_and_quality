#include <iostream>
#include <numbers>
 
using namespace std;

#define PI 3.141592653589793

 
// Base class
class Shape 
{
public:
   // pure virtual function providing interface framework.
   virtual int getArea() = 0;
   void setWidth(int w)
   {
 		width = w;
   }
   void setHeight(int h)
   {
      	height = h;
   }
   void setRadius(int r)
   {
   		radius = r;
   }
protected:
   int width;
   int height;
   int radius;
};
 
class Triangle: public Shape
{
public:
   int getArea()
   { 
      return (width * height)/2; 
   }
};

class Circle: public Shape
{
public:
	int getArea()
	{
		return PI * (radius * radius);
	}	
};
 
int main(void)
{
   Triangle  Tri;
   Circle cir;

   

   Tri.setWidth(5);
   Tri.setHeight(7);
   cir.setRadius(3);
   
   // Print the area of the object.
   cout << "Total Triangle area: " << Tri.getArea() << endl; 
   cout << "Total Circle area: " << cir.getArea() << endl;

   return 0;
}

