# for i in range()
#     print(i)

# saved_amount = int(input('Please enter your saved amount: '))

# saved_amount = 205
# ps4_price = 799

# if saved_amount <= ps4_price/2:
#     print("You must save more, keep saving!")
# elif saved_amount > ps4_price/2 and saved_amount < ps4_price:
#     print("You saved more than half, keep saving!")
# elif saved_amount >= ps4_price:
#     print("Yippee! You can buy your PS4")

# def sum_double(x, y):
#     if x == y:
#         return 2*(x+y)
#     else:
#         return x+y

# print(sum_double(1, 2))

# word = input("Please Enter a Country :").lower()
# vowels = ["a", "e", "i", "o", "u"]
# found = []

# for i in word:
#     if i in vowels:
#         found.append(i)

# print(set(found))

# word ="United States Of America"

# print(word.lower())

# a = []

# for i in range(100, 501):
#     if i % 7 == 0 and i % 3 == 0:
#         a.append(i)

# # print(a)


# a = []

# for i in range(100, 501):
#     if i % 21 == 0:
#         a.append(i)

# print(a)

a = input("Write sth:")
a = a.replace(" ", "")

dig = 0
let = 0

for i in a:
    if i.isdigit():
        dig += 1
    else:
        let += 1

print("Letters", let)
print("Digits", dig)