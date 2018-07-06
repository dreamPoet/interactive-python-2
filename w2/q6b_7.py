n = 1000
numbers = range(2, n)

results = []

while len(numbers) > 0:
    num = numbers.pop(0)
    results.append(num)
    
    i = 0
    while i < len(numbers):
        # print i, len(numbers)
        if numbers[i] % num == 0:
            numbers.pop(i)
        else:
            i += 1
    
            
print len(results)



# version 2


n = 1000
numbers = range(2, n)
results = []

while numbers != []:
    results.append(numbers[0])
    numbers = [n for n in numbers if n % numbers[0] != 0]

print len(results)