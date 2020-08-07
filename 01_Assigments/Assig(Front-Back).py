# word = input("write a word : ")

# def front_back(word):
#     word2 = list(word)
#     uzunluk = len(word2)
#     i = word2[0]
#     word2[0] = word2[uzunluk-1]
#     word2[uzunluk-1] = i
#     cikti = "".join(word2)
#     return cikti
# print(front_back(word))


def missing_char(word, n):
    word2 = list(word)
    word2[n] = ""
    cikti = "".join(word2)
    return cikti

print(missing_char("kitchen", 1))