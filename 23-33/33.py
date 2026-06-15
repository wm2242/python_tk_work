def main():
    number = int(input())
    print(f"正整数是{len(str(number))}位数")
    num_str = str(number)[::-1]
    print(num_str)
if __name__ == "__main__":
    main()