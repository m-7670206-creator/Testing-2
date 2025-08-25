strs = ["abc", "abcde", "abcdefg"]
prev = ""
common = []

for n, chr in enumerate(strs[0]):

    if chr in strs[1] and chr in strs[2]:
        prev = prev + chr

    elif prev not in common and prev:
        common.append(prev)

        prev = ""

    if n == len(strs[0]) - 1:
        common.append(prev)

longest = ""

for term in common:
    if len(term) > len(longest):
        longest = term
print(longest)

print("changed")
