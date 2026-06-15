def main():
    a, b = 2, 3
    c, d = 1, 2
    total = a / c
    for _ in range(19):
        total += b / d
        a, b = b, a + b
        c, d = d, c + d
    print(total)
if __name__ == '__main__':
    main()