import math
def main():
    def is_true(x):
        r = math.isqrt(x)
        return r * r == x
    m = 0
    while True:
        if is_true(m + 100) and is_true(m + 168):
            print(m)
            break
        m += 1

if __name__ == '__main__':
    main()