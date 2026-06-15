def main():
    numbers = []
    for i in range(0, 3):
        numbers.append(int(input("输入第%d个整数:" % (i + 1))))
    numbers.sort()
    print(*numbers)

if __name__ == "__main__":
    main()