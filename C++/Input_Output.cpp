#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;
//you don't need to include so many standard files but they were already included in the code in hackerrank
//for variable number of inuts
int main() {
    int n,sum = 0;
    while(cin>>n){
        sum +=n;
    }
    cout << sum << endl;
    return 0;
}
