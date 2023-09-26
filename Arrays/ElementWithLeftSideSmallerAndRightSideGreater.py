if __name__ == '__main__':
    arr = [4, 2, 5, 7]
    # arr = [11, 9, 12]
    midElement = arr[0]
    index = 0
    for i in range(0, len(arr) - 1):
        if midElement > arr[i + 1]:
            midElement = arr[i + 1]
            index = arr.index(midElement)

    if arr[index + 1] != arr[-1]:
        print(arr[index + 1])
    else:
        print("can't able to find the middle Element ")