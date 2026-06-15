import math
def main():
    for i in range(2, 1001):
        num = 1
        for j in range(2, math.isqrt(i) + 1):
            if i % j == 0:
                num += j
                if j != i // j:
                    num += i // j
        if num == i:
            print(i)

if __name__ == '__main__':
    main()