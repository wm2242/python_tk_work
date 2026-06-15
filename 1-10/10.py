def main():
    a = input("a = ")
    number = int(input("number = "))
    value_all = sum(int(a * i) for i in range(1, number + 1))
    print(value_all)

if __name__ == '__main__':
    main()