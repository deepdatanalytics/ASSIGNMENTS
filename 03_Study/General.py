# saved_amount = int(input('Please enter your saved amount: '))

# ps4_price = 400

# if saved_amount <= ps4_price/2:
#     print("You must save more, keep saving!")
# elif saved_amount > ps4_price/2 and saved_amount < ps4_price:
#     print("You saved more than half, keep saving!")
# elif saved_amount >= ps4_price:
#     print("Yippee! You can buy your PS4")

#

# while True:

#     math_mark = int(input('Please enter the mark: '))

#     if math_mark >= 85 and math_mark <= 100:
#         print("A (Excellent)")
#     elif math_mark >= 70 and math_mark <= 84:
#         print("B (Good)")
#     elif math_mark >= 60 and math_mark <= 69:
#         print("C (Medium)")
#     elif math_mark >= 45 and math_mark <= 59:
#         print("D (Not Bad)")
#     else:
#         print("F (Failed)")

# number = int(input("Please enter a number: "))

# b = 0

# while b < number:
#     print(b ** 2)
#     b += 1


#for i in range(number):
#    print(i ** 2)
        
# sample_list = [{"section":5, "topic":2}, 'clarusway', [1, 4], 2020, 3.14, 1+618j, False, (10, 20)]

# for i in sample_list:
#     print("The type of", i, "is", type(i))

# family_members = ['Meghan', 'Tom', 'Nicole', 'Tim']

# a = tuple(family_members)
# print(a)

# for i in range(12):
#     print(i)
#     if i == 9:
#         print("olay bitmiştir.")
#         break

# word = 'clarusway'
# n = 3
# front = word[:n]
# back = word[(n+1):]
# print(front + back)


# a = [1, 2, 3]

# b = [1, 3, 4, 5, 6, 6]

# print(1 in a)


# def texter(a, b, c):
#     print(f"{b} {c} {a}")

# # a= "i"
# # b= "love"
# # c= "you"

# texter(b="i", a="you", c="love")


# def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
#     print("-- This parrot wouldn't", action, end=' ')
#     print("if you put", voltage, "volts through it.")
#     print("-- Lovely plumage, the", type)
#     print("-- It's", state, "!")

# parrot("merhaba")


# even = []
# odd = []

# def slicer(*numbers):
#     for i in numbers:
#         if i % 2 == 0:
#             even.append(i)
#         else:
#             odd.append(i)

# slicer(1, 2, 3, 4, 5, 6, 7, 8, 9)
# print(even)
# print(odd)


# def organizer(**yeni):
#     names = [a for a in yeni.keys()]
#     ages = [a for a in yeni.values()]
#     print(names)
#     print(ages)

# organizer(Beth=26, OS=25, Zart=32, Zurt=34)


# def merger(a, b, c, d):
#     print(f"For me {a} {d} and {c} {b} are geniuses")

# genius = ("bill", "rossum", "guido van", "gates")
# merger(*genius)

# def meaner(a, b, c):
#     print((a+b+c)/3)

# friends = {a : 3, b : 4, c : 5}

# meaner(**friends)


# def kwar(1, 2):
#     print(x,  y, "denemesidir")

# sozluk = {"x" : "ikizim", "y" : "yeğim"}

# kwar(**sozluk)
# kwar("yeni", "deneme")


# bayan = {"f" :["marry", "bella", "susan"], "m" :["fred", "paul", "bahadir"]}

# def mur(f, m):
#     # a = [(f[0], m[0]), (f[1], m[1]), (f[2], m[2])]
#     x = zip(f, m)
#     print(list(x))

# mur(**bayan)


# def not_string(word):
#     if word.startswith("not"):
#         return word
#     else: return ("not"+word)

# print(not_string("not"))


# def team_names(*teams) :
#     print('The teams in Premier League are :')
#     for i in teams :
#         print('-', i)

# team_names('Liverpool', 'M.United', 'M.City', 'Arsenal')

# def make_sentence(**kwargs):
#     result = ""
#     # Iterating over the Python kwargs dictionary
#     for i in kwargs.values():
#         result += i
#     return result

# print(make_sentence(a="I ", b="love ", c="Clarusway!"))


# count = 1

# def counter():
#     global count 
#     count += 1
#     print(count)  

# counter()



# x = 'My name is Richard'
# def my_function_1(): 
#     x = 'My name is John'
    
# print(x)
  


# def outer():
#     x = "previous"
    
#     def inner():
#         nonlocal x
#         x = "later"
#         print("inner:", x)
    
#     inner()
#     print("outer:", x)

# outer()
# print(x)


# number_list=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# result= list(filter(lambda x: x % 2 != 0, number_list))   

# print(result)

# print((lambda x: x % 2 != 0)(3))


# x = 2

# def foo():
#     x = 2
#     print(x)

# foo()


# count = 123

# def x():
#     a = count + 1
#     print(a)

# x()


# def scope_test():
#     def do_local():
#         spam = "local spam"
 
#     def do_nonlocal():
#         nonlocal spam
#         spam = "nonlocal spam"
 
#     def do_global():
#         global spam
#         spam = "global spam"
 
#     spam = "test spam"
#     do_local()
#     print("After local assignment:", spam)
#     do_nonlocal()
#     print("After nonlocal assignment:", spam)
#     do_global()
#     print("After global assignment:", spam)
 
# scope_test()
# print("In global scope:", spam) 


# func = lambda x: x[::-1]
# print(func("abcd"))


# list = [1, 2, 3, 4]

# for i in list:
#     a = lambda x: "even" if x % 2 == 0 else "odd"
#     print(i, ":", a(i))

# print("sadfas")
# print('''birinci satırım
#             ikinci satırım''')



# toplacıkar = {"topla" : lambda x, y : x + y, "çıkar" : lambda x, y : x - y, "a" : 111, "b" : 222}

# toplacıkar.update({"a" : 111})

# # print(toplacıkar)

# word = "clarusc"

# word2 = list(word)

# print(word2)

# word2[0] = "s"

# print(word2)

# print(str(word2))

a = "a-b-c-d"

q, w, e, r = a.split("-")
print(q)
print(w)