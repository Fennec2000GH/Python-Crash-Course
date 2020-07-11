

// #pragma once
#include <cmath>
using namespace std;

extern "C"
{
float power(const int &base, const int &exponent) { 
    return pow(base, exponent);
}
}
