import random
def main():
    number = random.randint(0, 101)
    while True:
        a = int(input("输入0-100以内的整数:"))
        if a == number:
            print("你猜对了")
            break
        elif a > number:
            print("数字大了")
        else:
            print("数字小了")

if __name__ == "__main__":
    main()