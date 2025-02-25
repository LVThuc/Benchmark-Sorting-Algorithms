#include<bits/stdc++.h>
using namespace std;
mt19937 rng(chrono::steady_clock::now().time_since_epoch().count());
int random(int l, int r)
{
    return uniform_int_distribution<int>(l, r)(rng);
}
int ar[1000010];
int main()
{
    int n = 1e6;
    freopen("input.inp","w",stdout);
    for(int i = 1; i <= 1e6; i ++)
    {
        ar[i] = random(1,1e9);
    }
    sort(ar+1,ar+n+1);
    for(int i=1 ;i<= 1e6;i++)
    {
        cout<< ar[i] << ' ';
        ar[i] = random(1,1e9);
    }
    sort(ar+1,ar+n+1,greater<int>());
    cout<<'\n';
    for(int i=1 ;i<= 1e6;i++)
    {
        cout<< ar[i] << ' ';
    }
    cout<<'\n';
    for(int index = 3; index <= 10; index++)
    {
        for(int i = 1; i <= n; i++)
            cout << random(1, 1e9) << ' ';
        cout<<'\n';
    }
    return 0;
}