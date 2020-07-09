while True:
    number = input("Write a positive number: ")
    sum = 0
    if  not number.isdigit():
        print(" It is an invalid entry. Don't use non-numeric, float, or negative values!")
    elif int(number) <= 0:
        print(" It is an invalid entry. Don't use non-numeric, float, or negative values!")
    else:
        for i in number:
            sum += int(i) ** len(number)
        if sum == int(number):
            print(number, "is an Armstrong number")
            break
        else:
            print(number, "is not an Armstrong number")
            break