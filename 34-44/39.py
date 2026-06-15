import os
dir_path = "39"
txt_path = os.path.join(dir_path, "test.txt")
if not os.path.exists(dir_path):
    os.mkdir(dir_path)
    print("已创建文件夹")
else:
    print("目录已存在，跳过创建文件夹")
print("终止输入请打一个#")
print("请输入文本:")
with open(txt_path, 'a', encoding='utf-8') as file:
    while True:
        text = input()
        if text == "#":
            break
        elif text == "##":
            file.write("#\n")
        else:
            text = text.upper()
            file.write(text + "\n")
        file.flush()