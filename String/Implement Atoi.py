"""
Input:
str = 123
Output: 123


Input:
str = 21a
Output: -1
Explanation: Output is -1 as all
characters are not digit only.
"""


def Atoi(str):
    flag = False

    for char in str:
        if char.isdigit():
            flag = True
        else:
            flag = False

    return flag

if __name__ == '__main__':
    res = Atoi("123")
    if res == False:
        print(-1)
    else:
        print("its a Integer")