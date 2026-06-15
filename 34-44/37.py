def main():
    x = 10
    while True:
        if 809 * x < 10000 and 8 * x >= 10 and 9 * x >= 100:
            break
        x += 1
    print(f"??={x}")
    print(f"809*??={x * 809}")

if __name__ == "__main__":
    main()