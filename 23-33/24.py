import os
if not os.path.exists("24"):
    os.mkdir("24")
    print("已创建文件夹")
else:
    print("目录已存在，跳过创建文件夹")
file = open('24//text.txt', 'a+', encoding='utf-8')
file.write("Python程序设计基础\n")
file.seek(0)
text = file.read()
print(text)
file.close()