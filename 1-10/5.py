def main(month):
    baby, mid, adult = 1, 0, 0
    print("第%d年有%d只兔子" % (1, baby + mid + adult))
    for i in range(1, month):
        adult += mid
        mid = baby
        baby = adult
        print("第%d年有%d只兔子" % (i + 1, baby + mid + adult))

if __name__ == '__main__':
    main(11)
