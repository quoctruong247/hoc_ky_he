n = 3846739
a = 0
while n > 0 :
    a = a + n % 10
    n = n/10
print(a)