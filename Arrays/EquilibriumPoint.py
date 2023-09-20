"""
Title:Equilibrium Poin

Discription:
Given an array A of n positive numbers. The task is to find the first equilibrium point in an array.
Equilibrium point in an array is a position such that the sum of elements before it is equal to the sum of elements after it.
Note: Return equilibrium point in 1-based indexing. Return -1 if no such point exists.

Example- 1:
Input:
n = 5
A[] = {1,3,5,2,2}
Output:
3
Explanation:
equilibrium point is at position 3 as sum of elements before it (1+3) = sum of elements after it (2+2).

Example- 2:
Input:
n = 1
A[] = {1}
Output:
1
Explanation:
Since there's only element hence its only the equilibrium point.

"""

if __name__ == '__main__':
        arr = [1, 2, 1, 5, 2, 2]
        total_sum = sum(arr)
        left_sum = 0

        for i, num in enumerate(arr):
            print(num)
            total_sum -= num
            print(total_sum)
            if left_sum == total_sum:
                print("Equilibrium Point found at index:", i)
                break
            left_sum += num

        else:
            print("No equilibrium point found in the array")

