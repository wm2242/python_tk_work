def main():
    while True:
        number = int(input("输入一个奇数: "))
        if number > 0 and number % 2 == 1:
            break
    for i in range(1, number + 1, 2):
        print(" " * ((number - i) // 2), end="")
        print('*' * i)
    for i in range(number - 2, 0, -2):
        print(" " * ((number - i) // 2), end="")
        print('*' * i)

if __name__ == "__main__":
    main()