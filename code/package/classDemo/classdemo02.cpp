#include<iostream>
using namespace std;

const double pi = 3.14;

class Circle2
{
    public:
        double m_R;

        void setR(double r)
        {
            m_R = r;
        }

        double calclate()
        {
            return 2 * pi * m_R;
        }
};

void test()
{
    Circle2 c;
    c.setR(15);

    cout << c.calclate() << endl;
}

int main()
{
    test();

    return 0;
}
