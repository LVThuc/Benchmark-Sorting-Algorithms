#include <bits/stdc++.h>
using namespace std;
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
vector<int> test[10];
int main()
{
    auto ff = std::chrono::high_resolution_clock::now();
    freopen("input.inp", "r", stdin);
    for(int i = 0 ; i < 10 ; i++)
    {
        for(int j = 0 ;j < 1e6 ; j ++)
        {
            int x;
            cin>> x;
            test[i].push_back(x);
        }
    }
    ofstream f("built_inc++.json");
    f<<"[\n";
    for(int i = 0 ; i < 10 ; i++)
    {
        arr = test[i];
        auto start = std::chrono::high_resolution_clock::now();
        sort(arr.begin(), arr.end());
        auto finish = std::chrono::high_resolution_clock::now();
        f <<fixed << setprecision(5) << (double) std::chrono::duration_cast<std::chrono::nanoseconds>(finish-start).count()/(double)1000000.00 << ",\n";
    }
    f<<"]";
    f.close();
    auto fin =  std::chrono::high_resolution_clock::now();
    return 0;
}