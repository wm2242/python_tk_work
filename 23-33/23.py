import os
def main():
    with open('23/students.txt', 'r') as file:
        file.readline()
        while True:
            line = file.readline()
            if line == "":
                break
            name = line.split()[0] + line.split()[1]
            if not os.path.exists(f"23//{name}"):
                os.mkdir(f"23//{name}")
                print(f"已创建: {name}")
            else:
                print(f"目录已存在，跳过: {name}")
        file.close()

if __name__ == '__main__':
    main()