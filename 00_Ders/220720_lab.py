# x = int(input("write a number to calculate square root : "))

# iteration = int(input("How many iterations : "))

# r = x

# for i in range(iteration):
#     r = (r + x/r) / 2

# print(r) 

x = "Turkey"
vowels = ["a", "e", "i", "o", "u"]

for i in x:
    if i in vowels:
        x=x.replace(i, "")

print(x)