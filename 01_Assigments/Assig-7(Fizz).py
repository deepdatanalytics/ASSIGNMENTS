def fizbuzz():
    listemiz = []
    for i in range(0, 101):
        if i == 0:
            listemiz.append(i)
        elif i % 3 == 0 and i % 5 == 0:
            listemiz.append("FizzBuzz")
        elif i % 3 == 0:
            listemiz.append("Fizz")
        elif i % 5 == 0:
            listemiz.append("Buzz")
        else: listemiz.append(i)
    for x in listemiz:
        print(x)

fizbuzz()