"""
Given an array of N strings, find the longest common prefix among all strings present in the array.
Input:
N = 4
arr[] = {geeksforgeeks, geeks, geek,
         geezer}
Output: gee
Explanation: "gee" is the longest common
prefix in all the given strings.
"""

if __name__ == '__main__':

    def longest_common_prefix(arr):
        if not arr:
            return ""

        # Sort the array of strings to find the minimum and maximum strings
        arr.sort()
        min_str = arr[0]
        max_str = arr[-1]

        # Find the common prefix between the minimum and maximum strings
        n = min(len(min_str), len(max_str))
        i = 0
        while i < n and min_str[i] == max_str[i]:
            i += 1

        return min_str[:i]


    # Example usage
    arr = ["geeksforgeeks", "geeks", "geek", "geezer"]
    result = longest_common_prefix(arr)
    print("Longest common prefix:", result)  # Output will be "gee"
