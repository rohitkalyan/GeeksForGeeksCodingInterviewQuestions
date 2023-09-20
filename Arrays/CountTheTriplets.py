"""
Title: Count the triplets

Given an array of distinct integers. The task is to count all the triplets such that sum of two elements equals the third element.

Example-1:
Input:
N = 4
arr[] = {1, 5, 3, 2}
Output: 2
Explanation: There are 2 triplets:
 1 + 2 = 3 and 3 +2 = 5

Example-2:
Input:
N = 3
arr[] = {2, 3, 4}
Output: 0
Explanation: No such triplet exits

"""

if __name__ == '__main__':
    arr = [1, 5, 3, 2]
    # arr = [2, 3, 4]
    arr = sorted(arr)
    count = 0
    if len(arr) % 2 == 0:
        midIndexArr = int(len(arr) / 2 + 1)
    else:
        midIndexArr = int(len(arr) / 2)
    for i in range(0, len(arr) -1):
        sum = arr[i] + arr[i + 1]
        if sum in arr:
            count = count + 1
    if count == 0:
        print("No such triplet exits")
    else:
        print("There are "+ str(count) +" triplets")


