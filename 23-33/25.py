import math
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, math.isqrt(n) + 1):
        if n % i == 0:
            return False
    return True

def main():
    for i in range(1, 101):
        if is_prime(i):
            print(f"{i}是素数")

if __name__ == "__main__":
    main()