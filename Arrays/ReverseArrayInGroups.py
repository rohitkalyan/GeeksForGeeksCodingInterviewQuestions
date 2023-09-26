"""
Title: Reverse array in groups

Discription: Given an array arr[] of positive integers of size N. Reverse every sub-array group of size K.
    Note: If at any instance, there are no more subarrays of size greater than or equal to K, then reverse the last subarray (irrespective of its size).
    You shouldn't return any array, modify the given array in-place.

Example- 1:
Input:
N = 5, K = 3
arr[] = {1,2,3,4,5}
Output: 3 2 1 5 4
Explanation: First group consists of elements
1, 2, 3. Second group consists of 4,5.

Example- 2:
Input:
N = 4, K = 3
arr[] = {5,6,8,9}
Output: 8 6 5 9
"""


if __name__ == '__main__':
    # arr = [1,2,3,4,5]
    arr = [5,6,8,9]
    N = 5
    k = 3
    concatenated_array = []
    reverseArr = arr[:k]
    subArr2 = arr[k : ]
    concatenated_array.extend(reverseArr[::-1])
    concatenated_array.extend(subArr2)
    print(concatenated_array)