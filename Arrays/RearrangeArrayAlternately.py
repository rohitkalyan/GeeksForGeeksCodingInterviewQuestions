"""
Title: Rearrange Array Alternately

Discription:    Given a sorted array of positive integers. Your task is to rearrange the array elements alternatively
            i.e first element should be max value, second should be min value, third should be second max, fourth should be second min and so on.
            Note: Modify the original array itself. Do it without using any extra space. You do not have to return anything.

Example- 1:

Input:
n = 6
arr[] = {1,2,3,4,5,6}
Output: 6 1 5 2 4 3
Explanation: Max element = 6, min = 1,
second max = 5, second min = 2, and
so on... Modified array is : 6 1 5 2 4 3.

Example- 2:
Input:
n = 11
arr[]={10,20,30,40,50,60,70,80,90,100,110}
Output:110 10 100 20 90 30 80 40 70 50 60
Explanation: Max element = 110, min = 10,
second max = 100, second min = 20, and
so on... Modified array is :
110 10 100 20 90 30 80 40 70 50 60.


"""
def rearrange_alternatively(arr):
    n = len(arr)

    if n < 2:
        return  # Nothing to rearrange for arrays with less than 2 elements

    # Initialize pointers for the first and last elements
    start, end = 0, n - 1

    # Find the maximum element
    max_element = arr[end] + 1

    for i in range(n):
        if i % 2 == 0:
            # For even positions, put the maximum element
            arr[i] += (arr[end] % max_element) * max_element
            end -= 1
        else:
            # For odd positions, put the minimum element
            arr[i] += (arr[start] % max_element) * max_element
            start += 1

    # Extract the rearranged elements
    for i in range(n):
        arr[i] = arr[i] // max_element

def main():
    my_array = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    rearrange_alternatively(my_array)
    print(my_array)  # Output will be [9, 1, 8, 2, 7, 3, 6, 4, 5]

if __name__ == "__main__":
    main()
