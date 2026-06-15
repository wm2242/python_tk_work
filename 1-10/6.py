import math
def main():
    num = 0
    def is_true(x):
        for i in range(2, math.isqrt(x) + 1):
            if x % i == 0:
                return False
        return True

    for i in range(101, 201):
        if is_true(i):
            num += 1
            print("第%d个素数为%d" % (num, i))
    print("101到200之间共有%d个素数" % num)

if __name__ == "__main__":
    main()