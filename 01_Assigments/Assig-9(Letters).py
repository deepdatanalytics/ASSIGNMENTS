sentence = input("Write a sentence : ")

counted_dict = {}

for i in sentence:
    a = sentence.count(i)
    counted_dict.update({i : a})

print(counted_dict)
