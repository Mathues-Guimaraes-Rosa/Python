i = 1
a, b = 0 , 1

while (i <= 29):
    r = a + b
    a, b = b, a + b
    print(r)
    i += 1