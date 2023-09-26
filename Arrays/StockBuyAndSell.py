if __name__ == '__main__':
    arr = [100, 180, 260, 310, 40, 535, 695]
    # arr = [4, 2, 2, 2, 4]
    max_value = max(arr)
    max_index = len(arr) - 1 - arr[::-1].index(max_value)
    min_value = min(arr)
    min_index = len(arr) - 1 - arr[::-1].index(min_value)
    arr[max_index], arr[-1] = arr[-1], arr[max_index]
    arr[min_index], arr[-2] = arr[-2], arr[min_index]
    if max_index > min_index:
        print("Its a profit we can buy the stock in day: ", min_index, " And the sell the Stock in day: ", max_index)
    else:
        print("No Profit")
