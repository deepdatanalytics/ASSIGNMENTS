left = {"a", "q", "z", "w", "s", "x", "v", "t", "r", "d", "g", "f", "c"}
right = {"y", "n", "m", "j", "h", "b", "k", "u", "o", "l", "p"}

word = set(input("Wright a word to check if comfortable : "))

print(bool(word-left) and bool(word-right))