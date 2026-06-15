def main():
    number = int(input("输入一个正整数(平行四边形的底):"))
    high = int(input("输入一个正整数(平行四边形的高):"))
    for i in range(high, 0, -1):
        print(" " * (high - i), end="")
        print("*" * number)

if __name__ == "__main__":
    main()