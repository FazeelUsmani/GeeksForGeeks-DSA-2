/* Given an array arr[] of N integers arranged in a circular fashion. Your task is to find the maximum contiguous subarray sum.*/

int maxSubarraySumCircular(vector<int> &A)
{
    int total = 0, maxSum = A[0], curMax = 0, minSum = A[0], curMin = 0;
    for (int &a : A)
    {
        curMax = max(curMax + a, a);
        maxSum = max(maxSum, curMax);
        curMin = min(curMin + a, a);
        minSum = min(minSum, curMin);
        total += a;
    }
    return maxSum > 0 ? max(maxSum, total - minSum) : maxSum;
}