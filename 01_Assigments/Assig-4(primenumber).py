# number = int(input("Write a number to check if prime? : "))

# for i in range(2,1000000):
#     if i != number:
#         if number % i == 0:
#             print(number, "is not a prime number.")
#             break
#         elif i == 999999:
#             print(number, "is a prime number.")
#     elif i == number:
#         print(number, "is a prime number.")
#         break

number = int(input("Write a number to check if prime? : "))

if number == 1:
    print(number, "is not a prime number.")

else:
    for i in range(2,(number+1)):
        if i == number:
            print(number, "is a prime number.") 
        elif number % i == 0:
            print(number, "is not a prime number.")
            break
    
