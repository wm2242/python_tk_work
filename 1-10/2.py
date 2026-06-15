a = []
result = 0
for i in range(0, 5):
    num = int(input("请输入第%d个数:" % (i + 1)))
    a.append(num)
for i in range(0, 5):
    result += a[i]
print(result)