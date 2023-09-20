"""
Title: Count Inversions
Discription:Given an array of integers. Find the Inversion Count in the array.
            Inversion Count: For an array, inversion count indicates how far (or close) the array is from being sorted. If the array is already sorted then the inversion count is 0.
            If an array is sorted in the reverse order then the inversion count is the maximum.
            Formally, two elements a[i] and a[j] form an inversion if a[i] > a[j] and i < j.

Example- 1:
Input: N = 5, arr[] = {2, 4, 1, 3, 5}
Output: 3
Explanation: The sequence 2, 4, 1, 3, 5
has three inversions (2, 1), (4, 1), (4, 3).

Example- 2:
Input: N = 5
arr[] = {2, 3, 4, 5, 6}
Output: 0
Explanation: As the sequence is already
sorted so there is no inversion count.

"""

if __name__ == '__main__':
    arr = [10, 10, 10]
    # arr = [2, 3, 4, 5, 6]
    count = 0
    sortedArr = sorted(arr)
    for i in range(0, len(arr)):
        if arr[i] != sortedArr[i]:
         count += 1

    if count != 0:
        print(count - 1)
    else:
        print(count)