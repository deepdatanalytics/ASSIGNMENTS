# x = [1, 2, 3, 4][1]

# print(x)


# say = [22, 33, 55, 88, 2, 3, 9]
# çift = filter(lambda x: x % 2 == 0, say)
# print(list(çift))


# from earth import europe
# from earth.europe import kosovo, turkey

# print(dir(europe))

# kosovo.hello()
# turkey.topla(123, 3)

# print(europe.__spec__)

# print(dir(europe))



# from earth.europe import turkey

# turkey.topla(1323, 32)
# print(turkey.__doc__)


# import math
# print(math.__doc__)


# my_file = open("01_NOTLAR.txt", "r")

# for i in my_file.readlines():
#     print(i)

# my_file.close()


# with open("fruits.csv", "r", encoding="utf-8") as file:
#     print(file.read())


import csv 

with open("fruits.csv", "r", newline="", encoding="utf-8") as file:
    csv_rows = csv.reader(file)

    for row in csv_rows:
        print(row)