if __name__ == '__main__':
    # arr = [3, 30, 34, 5, 9]
    arr = [54, 546, 548, 60]
    stringArr = []
    largestNumberString = ""
    for i in arr:
        stringArr.append(str(i))
    stringArr.sort()
    stringArr.reverse()
    for i in stringArr:
        largestNumberString += i

    print(largestNumberString)