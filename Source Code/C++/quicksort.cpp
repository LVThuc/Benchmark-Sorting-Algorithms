#include <bits/stdc++.h>
using namespace std;
mt19937 rng(chrono::steady_clock::now().time_since_epoch().count());
int random(int a, int b)
{
    return a + rng() % (b - a + 1);
}
vector<int> arr;
int median_of_three(int low, int mid, int high) {
    if (arr[low] < arr[mid]) {
        if (arr[mid] < arr[high]) {
            return mid;
        } else if (arr[low] < arr[high]) {
            return high;
        } else {
            return low;
        }
    } else {
        if (arr[low] < arr[high]) {
            return low;
        } else if (arr[mid] < arr[high]) {
            return high;
        } else {
            return mid;
        }
    }
}

int partition(int low, int high) {
    int mid = low + (high - low) / 2;
    int pivot_index = median_of_three(low, mid, high);
    int pivot = arr[pivot_index];
    swap(arr[pivot_index], arr[high]);
    int i = low - 1;
    for (int j = low; j <= high - 1; j++) {
        if (arr[j] < pivot) {
            i++;
            swap(arr[i], arr[j]);
        }
    }
    swap(arr[i + 1], arr[high]);
    return i + 1;
}
void quickSort(int low, int high) {
  
    if (low < high) {
        int pi = partition(low, high);
        quickSort(low, pi - 1);
        quickSort(pi + 1, high);
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
    quickSort(0, n - 1);
}

