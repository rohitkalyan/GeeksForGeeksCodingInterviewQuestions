if __name__ == '__main__':
    # chocolates = [7, 3, 2, 4, 9, 12, 56]
    chocolates = [3, 4, 1, 9, 56, 7, 9, 12]
    m = 5
    fixedM = m
    lenghtOfChocolates = len(chocolates)
    diff = max(chocolates)
    chocolates = sorted(chocolates)
    i = 0
    while i < lenghtOfChocolates:
        slicedChocolates = chocolates[i:m]
        i += 1
        m += 1
        if len(slicedChocolates) == fixedM:
            sliceDiff = slicedChocolates[-1] - slicedChocolates[0]
            if diff > sliceDiff:
                diff = sliceDiff

    print("The min diffrence between the max and min cholates is: ", diff)



