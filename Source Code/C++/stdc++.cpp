#include <bits/stdc++.h>
using namespace std;
vector<int> arr;
int main()
{
    freopen("input.inp", "r", stdin);
    int n;
    cin >> n;
    arr.resize(n);
    for (int i = 0; i < n; i++)
        cin >> arr[i];
    sort(arr.begin(), arr.end());
    return 0;
}

