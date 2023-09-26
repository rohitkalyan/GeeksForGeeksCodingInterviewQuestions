"""
Title: Convert array into Zig-Zag fashion
Discription: To convert an array into a Zig-Zag fashion, you can sort the array in such a way that the elements alternate between
                being smaller and larger than their adjacent elements. Here's how you can do it in Python:
"""

if __name__ == '__main__':
    def zigzag(arr):
        n = len(arr)
        # Flag variable to indicate whether the current element should be smaller (True) or larger (False)
        is_smaller = True

        for i in range(n - 1):
            if is_smaller:
                # If the current element should be smaller, but it's larger, swap it with the next element
                if arr[i] > arr[i + 1]:
                    arr[i], arr[i + 1] = arr[i + 1], arr[i]
            else:
                # If the current element should be larger, but it's smaller, swap it with the next element
                if arr[i] < arr[i + 1]:
                    arr[i], arr[i + 1] = arr[i + 1], arr[i]
            is_smaller = not is_smaller


    arr = [4, 3, 7, 8, 6, 2, 1]
    zigzag(arr)
    print(arr)
