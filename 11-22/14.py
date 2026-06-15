def main():
    num = 0
    print("母鸡购买数量\t公鸡购买数量\t小鸡购买数量")
    for mj in range(0, 21):
        for gj in range(0, 34):
            xj = 100 - mj * 5 - gj * 3
            number = mj + gj + xj * 3
            if xj > 0 and number == 100:
                print("%d\t\t\t%d\t\t\t%d" % (mj, gj, xj * 3))
                num += 1
    print("有%d种买鸡方案" % num)

if __name__ == '__main__':
    main()