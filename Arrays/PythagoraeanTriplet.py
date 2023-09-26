"""
Title:
Discription:
Example- 1:
Example- 2:
"""

if __name__ == '__main__':
    arr = [3,2,4,6,5]
    is_sum_equal = lambda x, y, z: x**2 + y**2 == z**2
    result = [(x, y, z) for x in arr for y in arr for z in arr if is_sum_equal(x, y, z)]
    result = list(filter(lambda x: x[0] != x[1], result))
    result.sort()
    print(result[0])

