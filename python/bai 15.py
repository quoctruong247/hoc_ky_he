n = 3846739
total = 0
while n > 0 :
    if 8 % (n % 10)  == 0 :
        total = total + n % 10
    n = n/10
print(total)