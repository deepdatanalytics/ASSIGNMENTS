# try :
#     with open("aa.txt", "r") as a:
#         a.read()
# except FileNotFoundError:
#     print("There is not such a file or the path is incorrect.")


# while True:
#     no1 = 1
#     no2 = 0
#     try:
#         div = no1 / no2
#         print("a")
#         break
#     except Exception as e:
#         print("The problem is {}".format(e))
#         break


# try:
#     isim = input("isminiz : ")
#     4/0
# except Exception as e:
#     with open("hata.txt", "a", encoding= "utf-8") as bruce:
# #         bruce.write("{},{} \n".format(isim, e))

# import pandas as pd
# at = pd.read_csv("hata.txt")

# print(at[at["hata"]=="division by zero"])

# fruits = ["banana", "mango", "pear", "apple", "kiwi", "grape"]
# chance = 0

# while True:
#     try:
#         selection = int(input("Write the index number of your fav. fruit: "))
#         print("Your selection is {}".format(fruits[selection]))
#     except ValueError:
#         if chance < 3:
#             print("Please write a correct value")
#             chance += 1
#             print("You have {} right left.".format(3-chance))
#         else:
#             print("You have finished your chances good bye!")
#             break
#     except IndexError:
#         if chance < 3:
#             print("There is no such index")
#             chance += 1
#             print("You have {} right left.".format(3-chance))
#         else:
#             print("You have finished your chances good bye!")
#             break
#     else:
#         print("Congrats You have entered a valid input")
#     finally:
#         print("Our Fruits are great")


# xx = {"e" : 4, "b" : 2, "c" : 3, "f" : 1}

# sorteds = sorted(xx.items(), key=lambda x: x[1])

# print(sorteds)



my_list = [1, 2, 3, 4, 5]

print(list(x**2 for x in my_list))

print("x")