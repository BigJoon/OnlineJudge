#include <iostream>
#include <iomanip>

using namespace std;

int main(){

    long double a,b;

    cin >> a >> b ;
    std::cout << std::setprecision(32);
    long double c = a/b;
    std::cout << c << std::endl;

    return 0;
}
