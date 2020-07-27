# toplacıkar = {"topla" : lambda x, y : x + y, "çıkar" : lambda x, y : x - y, "a" : 111}

# print(toplacıkar["topla"](9, 3))


# hesap = {"+" : lambda x, y : x + y, "-" : lambda x, y : x - y, "/" : lambda x, y : x / y, "*" : lambda x, y : x * y}

# print(hesap["-"](8, 7))


# for x in [1,2,3,4,5]:
#     print(x, ":", (lambda x: "odd" if x % 2 != 0 else "even")(x))




# from datetime import datetime

# x = datetime.now()

# print(datetime.now().strftime("%Y"))
# print(x.strftime("%m"))
# print(x.strftime("%d"))


# benim = [1, 2, 3, 4, 5]

# print([str(i) for i in benim])

# dic = {str(i) + "'in karesi" : i ** 2 for i in range(6)}

# print(dic)


L = ["right 20", "right 30", "left 50", "up 10"]

x = 0 
y = 0 

for i in range(len(L)):
    if L[i].startswith("r") : x = x + int(L[i].split()[1])
    elif L[i].startswith("l") : x = x - int(L[i].split()[1])
    elif L[i].startswith("u") : y = y + int(L[i].split()[1])
    elif L[i].startswith("d") : y = y - int(L[i].split()[1])

print([x, y])
