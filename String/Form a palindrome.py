def min_insertions_to_make_palindrome(s):
    n = len(s)

    # Create a table to store the lengths of longest palindromic subsequences
    dp = [[0] * n for _ in range(n)]

    # Calculate longest palindromic subsequence lengths
    for i in range(n - 1, -1, -1):
        for j in range(i, n):
            if i == j:
                dp[i][j] = 1
            elif s[i] == s[j]:
                dp[i][j] = dp[i + 1][j - 1] + 2
            else:
                dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])

    # The minimum number of insertions needed is the difference between string length and its LPS length
    return n - dp[0][n - 1]


# Example
input_str = "abcd"
result = min_insertions_to_make_palindrome(input_str)
print("Output:", result)  # Output will be 3
