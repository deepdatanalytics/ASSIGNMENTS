# def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
#     print("-- This parrot wouldn't", action, end=' ')
#     print("if you put", voltage, "volts through it.")
#     print("-- Lovely plumage, the", type)
#     print("-- It's", state, "!")

# parrot(20, type="sdaf")                                          # 1 positional argument

# # print(7 ** 3 + 4 ** 3)

# number ="123"
# a = number.isdigit()
# print(a)


# fibonacci = []

# for i in range(-2, 8):
#     if i < 0 : fibonacci.append(1)
#     else : fibonacci.append(fibonacci[i]+fibonacci[i+1])

# print(fibonacci)

################   FİLTER() IN PYTHON   ####################

# letters = ["a", "b", "c", "d", "e", "i", "j", "x", "t"]

# def fltVowel(let):
#     vowel = ['a', 'e', 'i', 'o', 'u']
#     if let in vowel:
#         return True
#     else : 
#         return False

# filter(fltVowel, letters)
# filter()

################   TERNARY CONDITIONS IN PYTHON   ####################

# condition = True

# a = 134131 if condition else 0

# print(a)

# execute body1 if condition else execute body2

################   LIST COMPREHENSION IN PYTHON   ####################

# my_list = [1, 2, 3, 4, 5, 6]

# odd_sqr = []

# for x in my_list :
#     if x %2 != 0 :
#         odd_sqr.append(x ** 2)

# print(odd_sqr)

# for item in  iterable:
#     expression
        
# [expression for item in iterable]

# my_list = [1, 2, 3, 4, 5, 6]

# print([x ** 2 for x in my_list if x % 2 != 0])

# [x+1 for x in my_list]



# strings = ["ali", "veli", "ayşem"]

# [len(i) for i in strings]



# my_list = [1, 2, 3, 4, 5, 6]

# y = (x ** 2 for x in my_list)

# next(y)

# for i in y:
# #     print(i)

# # print([i for i in "clarusway"])

# [i for i in "beri gel berber" if i == "e"]

# [i for i in "beri gel berber" if i != "e" and i != " "]
# # print(0xA + 0xB + 0xC)
# print("abcd"[2:])

# a = "dsafs"
# b = "a"

# print(a - 3)

print("a" "b", 2)