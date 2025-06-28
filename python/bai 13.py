n = 3846739
total = 0
while n > 0 :
    if (n % 10) % 2  != 0 :
        total = total + n % 10
    n = n/10
print(total)