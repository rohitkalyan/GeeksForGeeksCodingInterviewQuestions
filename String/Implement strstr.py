"""
Your task is to implement the function strstr.
The function takes two strings as arguments (s,x) and  locates the occurrence of the string x in the string s.
The function returns an integer denoting the first occurrence of the string x in s (0 based indexing).
"""

if __name__ == '__main__':
    s = "GeeksForGeeks".lower()
    x = "f0r".lower()
    try:
        index = s.index(x)
        print(f"Substring found at index {index}.")
    except ValueError:
        print("Substring not found in the main string.")