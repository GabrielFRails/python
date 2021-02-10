numbers_pares = []
counter = 0

while(counter < 20):
    if(counter % 2 == 0 and counter != 0):
        numbers_pares.append(counter)
    counter += 1

print(numbers_pares)