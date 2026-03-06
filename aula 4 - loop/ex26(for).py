a, b = 0, 1
for i in range(1 , 30 , 1):
    r = a + b
    a , b = b , a + b
    print(r) 