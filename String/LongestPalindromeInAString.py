# str = "aaabbaa"
str = "babad"

def heightestIndexOfChar(str, charecterToFind):
    highest_index = -1
    for i in range(len(str)):
        if str[i] == charecterToFind:
            highest_index = i
    return highest_index + 1

for i in range(0, len(str)):
    endIndex = heightestIndexOfChar(str, str[i])
    subString = str[i:endIndex]
    if subString == subString[::-1]:
        print("The longest Palindromicsubstring is ", subString)
        break


