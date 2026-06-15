def main():
    year = int(input("输入年:"))
    month = int(input("输入月:"))
    day = int(input("输入日:"))
    mon = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    def is_true(year_is):
        if year_is % 400 == 0:
            return True
        if year_is % 100 == 0:
            return False
        if year_is % 4 == 0:
            return True
        return False
    value_day = sum(mon[0:month - 1]) + day
    if is_true(year) and month > 2:
        value_day += 1
    return value_day

if __name__ == "__main__":
    print("此日期是这一年的第%d天" % main())