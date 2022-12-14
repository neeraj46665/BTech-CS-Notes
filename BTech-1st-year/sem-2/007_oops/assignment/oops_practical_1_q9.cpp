#include<bits/stdc++.h>
using namespace std;
class Circle{
    public:
    void area(int radius){
        int areaa=3.14*radius*radius;
        cout<<"the area of circle is: "<<areaa<<endl;
    }
};
class Triangle{
    public:
    void area(int base,int height){
      int areaa=0.5*base*height;
      cout<<"area of trianle is :"<<areaa<<endl;
    }
    
};
class Square{
    public:
    void area(int side){
        int areaa=side*side;
        cout<<"area of square is :"<<areaa<<endl;
    }
};
int main(){
    Circle c;
    Triangle t;
    Square s;
    c.area(4);
    t.area(4,6);
    s.area(7);
    return 0;
}