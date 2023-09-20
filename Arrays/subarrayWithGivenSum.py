"""
Title: Subarray with given sum
Discription:
Given an unsorted array A of size N that contains only positive integers, find a continuous sub-array that adds to a given number S and return the left and right index(1-based indexing) of that subarray.
In case of multiple subarrays, return the subarray indexes which come first on moving from left to right.
Note:- You have to return an ArrayList consisting of two elements left and right. In case no such subarray exists return an array consisting of element -1.

Example-1
Input:
N = 5, S = 12
A[] = {1,2,3,7,5}
Output: 2 4
Explanation: The sum of elements
from 2nd position to 4th position
is 12.

Example-2
Input:
N = 10, S = 15
A[] = {1,2,3,4,5,6,7,8,9,10}
Output: 1 5
Explanation: The sum of elements
from 1st position to 5th position
is 15.
"""

def subarrayWithGivenSum():
    # A = [1,2,3,7,5]
    # s = 12
    A = [1,2,3,4,5,6,7,8,9,10]
    sum = 0
    s = 15
    subArray = []

    for i in range(0, len(A)):
        if sum <= s:
            sum = sum + A[i]
            subArray.append(A[i])
    subArray.remove(sum - s)
    print(A.index(subArray[0]) + 1, A.index(subArray[-1]) + 1)

if __name__ == '__main__':
    subarrayWithGivenSum()

