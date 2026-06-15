import random
a = []
result = 0
for i in range(0, 10):
    num = random.randint(0, 100)
    a.append(num)
for i in range(0, 10):
    print(a[i])
    result += a[i]
print(result)