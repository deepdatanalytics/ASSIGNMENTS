n = int(input("Write a number to list prime numbers : "))

prime_list = []

if n == 1:
    print(n, "is not a prime number.")

else:
    for i in range(2,(n+1)):
        for x in range(2, (i+1)):
            if x == i:
                prime_list.append(x)
                break                 
            elif i % x == 0:
                break

print(prime_list)