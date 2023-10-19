a = "amazon"
b = "azonam"

def rotate_clockwise(string):
    return string[-2:] + string[:-2]

def rotate_anticlockwise(string):
    return string[2:] + string[:2]


if rotate_clockwise(a) == b:
    print("String 'b' can be obtained by rotating 'a' 2 places clockwise.")
elif rotate_anticlockwise(a) == b:
    print("String 'b' can be obtained by rotating 'a' 2 places anticlockwise.")
else:
    print("String 'b' cannot be obtained by rotating 'a' 2 places anticlockwise and two places anti clockwise")
