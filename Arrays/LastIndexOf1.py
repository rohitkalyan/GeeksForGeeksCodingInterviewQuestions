if __name__ == '__main__':
    # s = "00001"
    s = "0000"
    arr = []
    for i in range(len(s)):
        arr.append(int(s[i]))

    max_value = max(arr)
    max_index = len(arr) - 1 - arr[::-1].index(max_value)
    if arr[max_index] == 1:
        print(max_index)
    else:
        print("No '1' is present the give string")
