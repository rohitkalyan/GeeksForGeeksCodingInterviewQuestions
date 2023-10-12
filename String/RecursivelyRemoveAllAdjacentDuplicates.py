str = "geeksforgeek"
newStr = ""

i = 0
j = 1

while(j < len(str)):
    if str[i] == str[j]:
        i += 2
        j += 2
    else:
        newStr += str[i]
        i += 1
        j += 1

if str[-2] != str[-1]:
    newStr = newStr + str[-1]

print(newStr)

