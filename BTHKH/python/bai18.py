n = 3846739
max = n % 10
while n > 0 :
    if (n % 10) > max:
        max = n % 10
    n = n/10
print(max)