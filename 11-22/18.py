def shift_char(ch, key):
    if 'a' <= ch <= 'z':
        return chr((ord(ch) - ord('a') + key) % 26 + ord('a'))
    elif 'A' <= ch <= 'Z':
        return chr((ord(ch) - ord('A') + key) % 26 + ord('A'))
    else:
        return ch

def encrypt(text, key=4):
    return ''.join(shift_char(ch, key) for ch in text)

def decrypt(text, key=4):
    return ''.join(shift_char(ch, -key) for ch in text)

def main():
    plain = input("请输入文本: ")
    cipher = encrypt(plain)
    print(f"加密后: {cipher}")
    choose_print = input("要解密,输入1,否则输入其他:")
    if choose_print == '1':
        print(f"解密后: {decrypt(cipher)}")

if __name__ == "__main__":
    main()