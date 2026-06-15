def main(high, count):
    print("球的初始高度为%f,反弹次数为%d" % (high, count))
    journey = 0.0
    while count > 0:
        journey += high
        count -= 1
        high /= 2
        journey += high
    print("落地时的路程为%f" % (journey - high))
    print("反弹时的高度为%f" % high)

if __name__ == '__main__':
    main(100.0, 10)