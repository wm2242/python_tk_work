def main():
    number = int(input())
    num_str = str(number)[::-1]
    if str(number) == num_str:
        print(f"{number}是回文数")
    else:
        print(f"{number}不是回文数")
if __name__ == "__main__":
    main()