import os          # 导入操作系统接口模块，用于文件路径操作
import sqlite3     # 导入 SQLite 数据库操作模块
import tkinter as tk        # 导入 Tkinter 基础模块，用于创建 GUI
from tkinter import ttk     # 导入 ttk 子模块，提供更现代的控件（Treeview、Combobox 等）
import tkinter.font as tk_font  # 导入字体模块，用于动态测量文本宽度


def auto_width(tree, column, font=None):
    """根据 Treeview 列中所有数据（含表头）的最大长度，自动调整列宽。

    Args:
        tree: ttk.Treeview 控件实例
        column: 列标识符（如 'sid', 's_name' 等）
        font: 用于测量文本宽度的字体对象，默认为 Arial 10 号
    """
    if font is None:
        font = tk_font.Font(family="Arial", size=10)
    # 获取表头文本的宽度
    header = tree.heading(column, 'text')
    max_width = font.measure(header)
    # 遍历该列所有行，找到最宽的内容
    for child in tree.get_children():
        value = tree.set(child, column)
        if value:
            width = font.measure(value)
            if width > max_width:
                max_width = width
    # 设置列宽（留 20px 边距）
    tree.column(column, width=max_width + 20, minwidth=50)


def main():
    """程序主入口：创建 GUI 窗口，提供学生信息的增删查改功能。"""
    root = tk.Tk()
    root.title("学生信息表")
    root.geometry("1000x500")  # 设置窗口初始大小

    # ==================== 数据库连接（全局） ====================
    # 获取当前脚本所在的目录，并拼接到数据库文件路径
    base_dir = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(base_dir, "data", "data.db")
    # 如果数据库文件不存在，则退出程序
    if not os.path.exists(db_path):
        print(f"数据库文件未找到: {db_path}")
        root.destroy()
        return
    # 连接数据库并创建游标
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # ==================== 上方输入区域 ====================
    input_frame = tk.Frame(root)
    input_frame.pack(side="top", fill="x", padx=5, pady=5)

    # 学号输入
    tk.Label(input_frame, text="学号").grid(row=0, column=0, padx=5)
    text_id = tk.Entry(input_frame)
    text_id.grid(row=0, column=1, padx=5)

    # 姓名输入
    tk.Label(input_frame, text="姓名").grid(row=0, column=2, padx=5)
    text_name = tk.Entry(input_frame)
    text_name.grid(row=0, column=3, padx=5)

    # 年龄输入
    tk.Label(input_frame, text="年龄").grid(row=0, column=4, padx=5)
    text_age = tk.Entry(input_frame)
    text_age.grid(row=0, column=5, padx=5)

    # 性别输入
    tk.Label(input_frame, text="性别").grid(row=0, column=6, padx=5)
    text_sex = tk.Entry(input_frame)
    text_sex.grid(row=0, column=7, padx=5)

    # 专业输入
    tk.Label(input_frame, text="专业").grid(row=0, column=8, padx=5)
    text_major = tk.Entry(input_frame)
    text_major.grid(row=0, column=9, padx=5)

    # ==================== 中间 Treeview 数据表格 ====================
    tree_frame = tk.Frame(root)
    tree_frame.pack(fill="both", expand=True)

    # 创建 Treeview 控件，显示 5 列：学号、姓名、年龄、性别、专业
    tree = ttk.Treeview(tree_frame, columns=('sid', 's_name', 'age', 'sex', 'major'), show='headings')
    tree.heading('sid', text='学号')
    tree.heading('s_name', text='姓名')
    tree.heading('age', text='年龄')
    tree.heading('sex', text='性别')
    tree.heading('major', text='专业')

    # 添加垂直和水平滚动条
    vsb = ttk.Scrollbar(tree_frame, orient="vertical", command=tree.yview)
    hsb = ttk.Scrollbar(tree_frame, orient="horizontal", command=tree.xview)
    tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
    tree.grid(row=0, column=0, sticky='nsew')
    vsb.grid(row=0, column=1, sticky='ns')
    hsb.grid(row=1, column=0, sticky='ew')
    tree_frame.grid_rowconfigure(0, weight=1)
    tree_frame.grid_columnconfigure(0, weight=1)

    # ==================== 功能函数定义 ====================

    def load_data():
        """从数据库加载所有学生记录，刷新 Treeview 显示。"""
        # 清空表格中现有数据
        for item in tree.get_children():
            tree.delete(item)
        # 查询全部数据
        cursor.execute("SELECT * FROM test")
        rows = cursor.fetchall()
        # 逐行插入到表格
        for row in rows:
            tree.insert("", "end", values=row)
        # 自动调整各列宽度
        for col in tree['columns']:
            auto_width(tree, col)

    # 程序启动时加载已有数据
    load_data()

    def insert_data():
        """将输入框中的信息插入到数据库，并刷新表格显示。"""
        new_id = text_id.get().strip()
        name = text_name.get().strip()
        if not name:
            return  # 姓名为空时取消插入
        try:
            age = int(text_age.get())
        except ValueError:
            age = 0  # 年龄非数字时默认 0
        sex = text_sex.get().strip()
        major = text_major.get().strip()

        try:
            # 执行 INSERT 语句
            cursor.execute(
                "INSERT INTO test (sid, s_name, age, sex, major) VALUES (?, ?, ?, ?, ?)",
                (new_id, name, age, sex, major))
            conn.commit()
            # 直接在表格末尾追加一行
            tree.insert("", "end", values=(new_id, name, age, sex, major))
            # 清空输入框
            text_id.delete(0, tk.END)
            text_name.delete(0, tk.END)
            text_age.delete(0, tk.END)
            text_sex.delete(0, tk.END)
            text_major.delete(0, tk.END)
            # 重新调整各列宽度
            for col in tree['columns']:
                auto_width(tree, col)
        except sqlite3.Error as e:
            print(f"插入失败: {e}")

    def delete_data():
        """删除 Treeview 中选中的学生记录（按学号删除）。"""
        selected = tree.selection()
        if not selected:
            return  # 未选中任何行则不做操作
        values = tree.item(selected[0], 'values')
        sid = int(values[0])       # 获取选中学号
        cursor.execute("DELETE FROM test WHERE sid = ?", (sid,))
        conn.commit()
        load_data()  # 刷新表格

    def select_data():
        """按指定条件查询学生记录，支持严格匹配和模糊查询。"""
        # 获取查询条件
        attr = head.get()                # 查询属性（中文，如"学号"、"姓名"）
        keyword = select_value.get().strip()
        strict = (select_chose.get() == 0)  # 0 = 严格查询, 1 = 近似查询

        # 将中文属性名映射为数据库列名
        col_map = {
            "学号": "sid",
            "姓名": "s_name",
            "年龄": "age",
            "性别": "sex",
            "专业": "major"
        }
        col = col_map.get(attr)
        if not col or not keyword:
            print("请选择查询属性和输入关键词")
            return

        # 根据查询模式构造不同的 SQL 和参数
        if strict:
            # 严格查询（使用 = 精确匹配）
            if col in ("sid", "age"):
                # 学号和年龄需要转为整数
                try:
                    val = int(keyword)
                except ValueError:
                    print("学号和年龄必须为数字")
                    return
                sql = f"SELECT * FROM test WHERE {col} = ?"
                param = (val,)
            else:
                sql = f"SELECT * FROM test WHERE {col} = ?"
                param = (keyword,)
        else:
            # 近似查询（使用 LIKE 和 % 通配符）
            sql = f"SELECT * FROM test WHERE {col} LIKE ?"
            param = (f"%{keyword}%",)

        # 执行查询
        try:
            cursor.execute(sql, param)
            rows = cursor.fetchall()
        except sqlite3.Error as e:
            print(f"查询失败: {e}")
            return

        # 清空表格并显示查询结果
        for item in tree.get_children():
            tree.delete(item)
        for row in rows:
            tree.insert("", "end", values=row)
        # 自动调整列宽
        for col in tree['columns']:
            auto_width(tree, col)

    # ==================== 底部按钮区域 ====================
    btn_frame = tk.Frame(root)
    btn_frame.pack(side="bottom", fill="x", pady=5)

    # 主操作按钮一行
    tk.Button(btn_frame, text="插入数据", command=insert_data).grid(padx=5, row=0, column=0)
    tk.Button(btn_frame, text="删除数据", command=delete_data).grid(padx=5, row=0, column=1)
    tk.Button(btn_frame, text="刷新列表", command=load_data).grid(padx=5, row=0, column=2)
    tk.Button(btn_frame, text="查询数据:", command=select_data).grid(padx=5, row=0, column=4)

    # 查询条件第二行：属性下拉框、关键词输入、近似/严格单选框
    tk.Label(btn_frame, text="查询属性").grid(row=1, column=2)
    head = tk.StringVar()
    ttk.Combobox(btn_frame, width=5, textvariable=head, values=["学号", "姓名", "年龄", "性别", "专业"]).grid(row=1, column=3)
    select_value = tk.Entry(btn_frame, width=14)
    select_value.grid(row=1, column=4)
    select_chose = tk.IntVar()
    tk.Radiobutton(btn_frame, variable=select_chose, value=1, text="近似查询").grid(row=1, column=5)
    tk.Radiobutton(btn_frame, variable=select_chose, value=0, text="严格查询").grid(row=1, column=6)

    # 窗口关闭时关闭数据库连接
    def on_closing():
        conn.close()
        root.destroy()
    root.protocol("WM_DELETE_WINDOW", on_closing)

    # 进入 Tkinter 主事件循环
    root.mainloop()


if __name__ == '__main__':
    main()