def main():
    peach = j = 4
    flag = True
    while flag:
        for i in range(1, 6):
            if j % 4 != 0:
                peach += 4
                j = peach
                break
            j = j * 5 // 4 + 1
            if i == 5:
                flag = False
    print(f"最少有{j}个桃子")

if __name__ == "__main__":
    main()