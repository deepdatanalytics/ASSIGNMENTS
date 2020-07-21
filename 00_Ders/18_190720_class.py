# a = (lambda x : x ** 2)(3)
# print(a)

# average = lambda x, y: (x+y)/2
# print(average(3, 5))


# fonk = lambda x: 

# print(fonk("abcd"))


# def kare(a):

#     for i in x:
#         a=i**2
#         liste.append(a)


# nums1 = [9, 6, 7, 4]
# nums2 = [3, 6, 5, 8]

# arit = map(lambda x, y: (x+y)/2, nums1, nums2)
# print(list(arit))


# list1 = ["you", "much", "hard"]
# list2 = ["i", "you","he"]
# list3 = ["love", "ate", "works"]

# a = map(lambda x, y, z: y + " " + z + " " + x, list1, list2, list3)

# for i in a:
#     print(i)


# words = ["apple", "swim", "clock", "me", "kiwi", "banana"]

# a = filter(lambda x: len(x)<5, words)

# for i in a:
#     print(i)


# first_ten = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
# vowels = ["a", "e", "i", "o", "u"]

# a = filter(lambda x: x in vowels, first_ten)
# print(list(a))


# a = lambda x: x**2

# print(a(2))


#########################################################################


# def repeater(n):
#     return lambda x: print(x * n)

# repeat_2 = repeater(2)

# repeat_3 = repeater(3)

# repeat_4 = repeater(4)

# repeat_2("alex ")
# repeat_3("alex ")
# repeat_4("alex ")


# def x():
#     return 1,2,3,4

# # for i in x():
#     print(i)

# print(type(x()))



# def func_generator(function):
#     return lambda x: function(x)

# my_print = func_generator(print)
# my_max = func_generator(max)
# my_bool = func_generator(bool)
# my_sorted = func_generator(sorted)

# my_print("hello world")
# print(my_max([2, 5, 9, 11]))
# print(my_bool([]))
# print(my_sorted([3,1,9,12]))



# (lambda x: print(max(x)))([1, 3, 4, 324])


# def equal(a, b, c):
#     numbers = [a, b, c]
#     res = numbers.count(max(numbers, key=numbers.count))
#     return res if res > 1 else 0

# print(equal(3,3,3))



# equal = lambda x, y, z: [x, y, z].count(max[x,y,z] key=[x, y, z].count) if [x, y, z].count(max[x,y,z] key=[x, y, z].count) > 1 else 0
# print(equal(3,3,3))



# from math import pi, factorial, log10

# print(pi)
# print(factorial(3))
# print(log10(1000))


# import string

# print(string.punctuation)
# print(string.digits)


# import datetime

# print(dir(datetime))


# from datetime import date.today

# print(date.today())

# # import datetime

# print(datetime.date.today())


# from random import choice

# city= ["a", "b", "c", "d"]

# print(choise(city))


# from datetime import date
# birth = date(1993, 5, 27)
# bugün = date(2020, 7, 19)

# days = date.toordinal(bugün) - date.toordinal(birth)
# print(days)