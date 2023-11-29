romanList = {
    "I" : 1,
    "V" : 5,
    "X" : 10,
    "L" : 50,
    "C" : 100,
    "D" : 500,
    "M" : 1000,
}
str = "VI"
sum = 0

for i in range(len(str)):
    if i + 1 < len(str) and romanList[str[i]] < romanList[str[i + 1]]:
        sum -= romanList[str[i]]
    else:
        sum += romanList[str[i]]

print("This is the Sum: ", sum)
