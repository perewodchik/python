#include <iostream>
#include <vector>
#include <algorithm>
#include <iomanip>
#define VI vector<int>
#define ll longlong int


using namespace std;



int main()
{
	
	freopen("equations.in", "r", stdin);
	freopen("equations.out", "w", stdout);
	int n,sum;
	long long a,b,c, mod;
	sum = 0;
	cin >> n;
	for(int i = 0; i < n; i++)
	{
		cin >> a >> b >> c;
		mod = c-b;
		if( (a != 0) && (mod % a == 0) && ((mod)/a >= 0)  )
			sum++;		
		
		if((a==0 ) && (b==c)) 
			sum++;
	}
	
	cout << sum;
	return 0;
}

