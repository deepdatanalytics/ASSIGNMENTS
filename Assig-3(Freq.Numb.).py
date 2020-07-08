numbers = [1,3,7,4,3,0,3,6,3]

freq_number = max(numbers, key=numbers.count)

times = numbers.count(freq_number)

print(f"The most frequent number is {freq_number} and it was {times} repeated")