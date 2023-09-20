"""
Title: Number of pairs
Discription: Given two arrays X and Y of positive integers, find the number of pairs such that xy > yx (raised to power of) where x is an element from X and y is an element from Y.

Example- 1:
Input:
M = 3, X[] = [2 1 6]
N = 2, Y[] = [1 5]
Output: 3
Explanation:
The pairs which follow xy > yx are
as such: 21 > 12,  25 > 52 and 61 > 16.

Example- 2:
Input:
M = 4, X[] = [2 3 4 5]
N = 3, Y[] = [1 2 3]
Output: 5
Explanation:
The pairs for the given input are
21 > 12 , 31 > 13 , 32 > 23 , 41 > 14 ,
51 > 15.
"""


if __name__ == '__main__':
    # X = [2, 1, 6]
    X = [2, 3, 4, 5]
    Y = [1, 2, 3]
    # Y = [1, 5]
    count = 0

    for i in range(0, len(X)):
        for j in range(0, len(Y)):
           x = X[i]
           y = Y[j]
           if pow(x, y) > pow(y, x):
               count += 1

    print(count)
