import os

def main():
    with open('students.txt', 'r', encoding='utf-8') as file:
        file.readline()
        while True:
            line = file.readline()
            if line == "":
                break
            parts = line.split('\t')
            if len(parts) >= 2:
                name = parts[1] + parts[0]
                dir_path = f"23/{name}"
                if not os.path.exists(dir_path):
                    os.mkdir(dir_path)
                    print(f"已创建: {name}")
                else:
                    print(f"目录已存在，跳过: {name}")

if __name__ == '__main__':
    main()