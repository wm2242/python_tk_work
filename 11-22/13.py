def main():
    number = 1
    for day in range(9, 0, -1):
        number += 1
        number *= 2
    print(number)

if __name__ == '__main__':
    main()
