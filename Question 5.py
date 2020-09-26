for i in range(1,3000):
    for j in range(1,11):
        if i%j != 0:
            break
        else:
            continue

num = 2520
i = 2

while i < 21:
    if num%i == 0:
        i += 1
    else:
        num += 1
        i = 2
        
print(num)