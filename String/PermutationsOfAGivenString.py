def get_permutations(s):
    if len(s) == 1:
        return [s]
    permutations = []
    for i in range(len(s)):
        char = s[i]
        remaining = s[:i] + s[i + 1:]
        for perm in get_permutations(remaining):
            permutations.append(char + perm)
    return permutations

input_string = "ABC"
permutations = get_permutations(input_string)

print("Permutations of", input_string, "are:")
for perm in permutations:
    print(perm)
