# with open("fruits.csv", "r", encoding="utf-8") as file:
#     print(file.read())


# with open("people.csv", "w", encoding="utf-8") as people:
#     people.write("row number,first name,last name,ages\n")
#     people.write("1,isabella,bold,22\n")
#     people.write("2,lara,bold,52\n")
#     people.write("3,solomon,bold,42\n")
#     people.write("4,adam,bold,24\n")
#     people.write("5,mose,bold,23\n")

# with open("people.csv", "r", encoding="utf-8") as people:
#     print(people.read())


# import csv

# with open("people.csv", "r", newline="", encoding="utf-8") as file:
#     csv_rows = csv.reader(file, delimiter= " ")

#     for row in csv_rows:
#         print(row)


# import csv

# with open("fruits.csv", "r", newline="", encoding="utf-8") as file:
#     csv_rows = csv.reader(file, delimiter = " ")

#     print(list(csv_rows)[1:5])

# import pandas as pd

# df = pd.read_csv("fruits.csv", )

# print("Dont say I never make a mistake'"


# import math

# print(math.log10("x"))



while True:
    no_one = int(input("The first number please : "))
    no_two = int(input("The second number please : "))
    try:
        division = no_one / no_two
        print("The result of the division is : ", division)
        break
    except:
        print("Sth wrong try again")


