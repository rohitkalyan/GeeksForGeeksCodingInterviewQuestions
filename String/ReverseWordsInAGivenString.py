if __name__ == '__main__':
    s = "i.like.this.program.very.much"
    resultString = ""
    arr = s.split(".")
    arr.reverse()
    for i in arr:
        resultString += i
        resultString += "."
    print(resultString)

