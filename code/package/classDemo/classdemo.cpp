#include<iostream>
using namespace std;

const double pi = 3.14;
//设计一个圆类，求周长
class Circle
{
private:
    /* data */
public:
    //求周长
    double calclate()
    {
        return 2 * pi * m_R;
    }

    //半径
    int m_R;
    Circle
    (/* args */);
    ~Circle
    ();
};

Circle::Circle(/* args */)
{
}

Circle::~Circle()
{
}

void test01()
{
    Circle cl;
    cl.m_R = 20;

    cout << "周长" << cl.calclate() << endl;

}
int main()
{
    /* code */
    test01();
    return 0;
}

