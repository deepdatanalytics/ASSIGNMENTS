# sea = open("fishes.txt", "r")

# print(sea.readline())

# sea.close()

# a = open("fishes.txt", "r")

# for i in a.readlines():
#     print(i)

# a.close()



# a = open("fishes.txt", "r")

# for i in a:
#     print(i[:-1])

# a.close()


# with open("fishes.txt", "r", encoding="utf-8") as file:
#     print(file.readlines())


# with open("fishes.txt", "r") as sea:
#     print(sea.readline(13))
#     print(sea.readline(13))
#     print(sea.readline(13))
#     print(sea.readline(13))



# with open("fishes.txt", "r") as sea:
#     print(sea.readline())
#     print(sea.readlines())


# with open("dummy2.txt", "a") as file:
#     file.write("\nBu da en yenisi")

# with open("dummy2.txt", "r") as file:
#     print(file.read())


# fruits = ["banana", "orange", "apple", "strawberry", "cherry"]

# with open("fruits.txt", "w") as a:
#     for i in fruits:
#         a.write(i+"\n")

# with open("fruits.txt", "r") as a:
#     print(a.read())

# with open("fruits.txt", "r") as a:
#     print(a.readlines())


# flowers = ["Jasmine", "Rose", "Lily", "Daisy", "Tulip"]

# with open("flowers.txt", "w") as a:
#     for i in flowers:
#         a.write(i+ "\n\n")

# with open("flowers.txt", "r") as a:
#     print(a.read())


# fruits = ["banana\n", "orange\n", "apple\n", "strawberry\n", "cherry\n"]

# with open("fruits.txt", "w", encoding="utf-8") as file:
#     file.writelines(fruits)

# with open("fruits.txt", "r", encoding="utf-8") as file:
#     print(file.read())

# with open("fruits.txt", "r", encoding="utf-8") as file:
#     print(file.readlines())



# flowers = ["Jasmine\n", "Rose\n", "Lily\n", "Daisy\n", "Tulip\n"]

# with open("flowers.txt", "w") as a:
#     a.writelines(flowers)

# with open("flowers.txt", "r") as a:
#     print(a.read())


# fruits = ["banana\n", "orange\n", "apple\n", "strawberry\n", "cherry\n"]

# with open("fruits.txt", "a", encoding="utf-8") as file:
#     file.write("melon\n")

# with open("fruits.txt", "r", encoding="utf-8") as file:
#     print(file.read())

# with open("fruits.txt", "r", encoding="utf-8") as file:
#     print(file.readlines())




# flowers = ["Jasmine\n", "Rose\n", "Lily\n", "Daisy\n", "Tulip\n"]


# with open("flowers.txt", "a") as a:
#     a.seek(0)
#     a.write("orchid")

# with open("flowers.txt", "r") as a:
#     print(a.read())


count = 0

with open("istiklal.txt", "r", encoding="utf-8") as a:
    global x
    x = a.readlines()

with open("istiklal.txt", "w", encoding="utf-8") as a:
    for i in x:
        count += 1
        if count %4 == 0:
            a.write(i +"\n")
        else:
            a.write(i)
        
with open("istiklal.txt", "r", encoding="utf-8") as a:
    print(a.read())