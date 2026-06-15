import os
import sys
def main():
    dir_path = "38"
    txt_path = os.path.join(dir_path, "test.txt")
    if not os.path.exists(dir_path):
        os.mkdir(dir_path)
        print("已创建文件夹")
    else:
        print("目录已存在，跳过创建文件夹")
    with open(txt_path, 'a', encoding='utf-8') as f:
        print("开始输入(输入 # 结束):")
        while True:
            char = sys.stdin.read(1)   # 读取一个字符
            if char == '#':
                break
            f.write(char)
            f.flush()
    print("文件已保存。")

if __name__ == "__main__":
    main()