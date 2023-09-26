if __name__ == '__main__':
    # arr = [3,0,0,2,0,4]
    arr = [7,4,0,9]
    blockSize = arr[0]
    sum = 0
    for i in range(1, len(arr)-1):
        sum += blockSize - arr[i]

    print(sum)