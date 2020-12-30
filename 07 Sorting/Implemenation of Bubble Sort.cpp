/*
 * Author : Siddhant Khare
 */

#include <iostream>
#include <vector>
using namespace std;

int main()
{
    int n;
    bool swap_check = true;

    cin >> n;
    vector<int> numbers;

    int num;

    // Input
    for (int i = 0; i < n; i++) {
        cin >> num;
        numbers.push_back(num);
    }

    // Bubble Sorting
    for (int i = 0; (i < n) && (swap_check); i++) {
        swap_check = false;
        for (int j = 0; j < n - 1 - i; j++) {
            if (numbers[j] > numbers[j + 1]) {
                swap_check = true;
                swap(numbers[j],
                    numbers[j + 1]); // by changing swap location.
                                     // I mean, j. If the number is
                                     // greater than j + 1, then it
                                     // means the location.
            }
        }
    }

    for (int i = 0; i < numbers.size(); i++) {
        if (i != numbers.size() - 1) {
            cout << numbers[i] << " ";
        } else {
            cout << numbers[i] << " ";
        }
    }
    return 0;
}
