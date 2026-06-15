def main():
    text_str = input("请输入文本:")
    letters = numbers = spaces = others = 0
    for char in text_str:
        if char.isdigit():
            numbers += 1
        elif char.isalpha():
            letters += 1
        elif char.isspace():
            spaces += 1
        else:
            others += 1
    print("字母%d个,数字%d个,空字符%d个,其他符号%d个" % (letters, numbers, spaces, others))

if __name__ == '__main__':
    main()
