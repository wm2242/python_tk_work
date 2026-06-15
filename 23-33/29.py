def main():
    n = int(input())
    while True:
        if n % 10 == 0:
            n = int(input())
            continue
        else:
            break
    str_n = str(n)
    number = int("".join(ch for ch in str_n[::-1]))
    print(number)

if __name__ == "__main__":
    main()