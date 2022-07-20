import string


# My case
def is_pangram(s):
    count = 0
    alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "u", "v",
                "w", "x", "y", "z"]

    for x in alphabet:
        if s.__contains__(x) or s.__contains__(x.upper()):
            count += 1
    return count == len(alphabet)


# Best case
def is_pangram_bc(s):
    return set(string.ascii_lowercase).issubset(s.lower())


print(is_pangram("The quick brown fox jumps over the lazy dog"))
