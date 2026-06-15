import math
def commission_rule(number):
    value_rule = [(10,0.1), (10,0.075), (20,0.05), (20,0.03), (40,0.015), (math.inf,0.01)]
    commission = 0
    for value in value_rule:
        if number < value[0]:
            commission += value[1] * number
            break
        else:
            commission += value[0] * value[1]
            number -= value[0]
    return commission
def main():
    number = int(input("输入销售金额(单位为万元): "))
    print(f"销售提成为{commission_rule(number)}万元")

if __name__ == "__main__":
    main()
