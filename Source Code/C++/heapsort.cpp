#include <bits/stdc++.h>
using namespace std;
vector<int> arr;
void heapify(int n, int i){

    int largest = i;
    int l = 2 * i + 1;
    int r = 2 * i + 2;
    if (l < n && arr[l] > arr[largest])
        largest = l;
    if (r < n && arr[r] > arr[largest])
        largest = r;
    if (largest != i) {
        swap(arr[i], arr[largest]);
        heapify(n, largest);
    }
}
void heapSort(){
    int n = arr.size();
    for (int i = n / 2 - 1; i >= 0; i--)
        heapify(n, i);
    for (int i = n - 1; i > 0; i--) {
        swap(arr[0], arr[i]);
        heapify(i, 0);
    }
}
int main()
{
    freopen("input.inp", "r", stdin);
    int n;
    cin >> n;
    arr.resize(n);
    for (int i = 0; i < n; i++)
        cin >> arr[i];
    heapSort();
    return 0;
}