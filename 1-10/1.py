num = 0
for i in range(0, 101):
    if i % 3 == 0 or i % 5 == 0 or i % 7 == 0:
        num += i
print(num)