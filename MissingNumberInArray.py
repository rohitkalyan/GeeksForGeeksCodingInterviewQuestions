"""
Title: Missing number in array

Discription: Given an array of size N-1 such that it only contains distinct integers in the range of 1 to N. Find the missing element.

Example- 1:
Input:
N = 5
A[] = {1,2,3,5}
Output: 4

Example- 2:
N = 10
A[] = {6,1,2,8,3,4,7,10,5}
Output: 9
"""

if __name__ == '__main__':
    arr = [1, 2, 3, 5]
    arr = sorted(arr)

    for i in range(0, len(arr)-1):
        nextElement = arr[i] + 1
        if nextElement not in arr:
            print(nextElement)