#include <iostream>
#include <vector>
#include <algorithm>
#include <iomanip>
#include <string>

#define VI vector<int>
#define ll longlong int

using namespace std;

vector<bool> handler(string str)
{
	vector<bool> result;
	for(int i = 0; i < str.size(); i++)
	{
		if(str[i] == '#')
		{
			result.push_back(true);
		}
		else
			result.push_back(false);
	}
	return result;
}

int main()
{
	freopen("crossword.in", "r", stdin);
	freopen("crossword.out", "w", stdout);
	int n,m;
	cin >> n >>m;
	vector< vector<bool> > cross;
	
	string a;
	for(int i = 0; i < n; i++)
	{
		cin >> a;
		cross.push_back( handler(a) );
	}
	
	int streak;
	bool on_streak;
	bool returned_something;
	for(int i = 0; i < n; i++)
	{
		returned_something = false;
		streak = 0;
		on_streak = false;
		for(int j = 0; j < m; j++)
		{
			if(cross[i][j])
			{
				on_streak = true;
				streak++;
			}
			else
			{
				on_streak = false;
				if(streak)
				{
					cout << streak << " ";
					streak = 0;
					returned_something = true;
				}
			}
		}
		if(!returned_something || on_streak)
			cout << streak;
		cout << endl;
	}
	
	for(int j = 0; j < m; j++)
	{
		streak = 0;
		on_streak = false;
		returned_something = false;
		for(int i = 0; i < n; i++)
		{
			if(cross[i][j])
			{
				on_streak = true;
				streak++;
			}
			else
			{
				on_streak = false;
				if(streak)
				{
					cout << streak << " ";
					streak = 0;
					returned_something = true;
				}
			}
		}
		if(!returned_something || on_streak)
			cout << streak;
		cout << endl;
	}
	
	
	
	
}
