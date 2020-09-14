#include <iostream> // std:: fixed
#include <iomanip> // std::setprecision
using namespace std;
int main()
{
    int a; long b; char c; float d; double e;
    cin>>a>>b>>c>>d>>e;
    cout<<a<<"\n"<<b<<"\n"<<c<<"\n";
    /*Fixed is used to sets the floatfield format flag for the str stream to fixed. When floatfield is set to fixed, floating-point values are written using fixed-point notation: the value is represented with exactly as many digits in the decimal part as specified by the precision field (precision) and with no exponent part.
    Setprecision is used to set control the number of digits of an output stream*/
    cout<<fixed<<setprecision(3)<<d<<"\n"; 
    cout<<fixed<<setprecision(9)<<e<<"\n";
    return 0;
}
