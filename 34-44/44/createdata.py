import sqlite3  # 导入 SQLite 数据库操作模块
import os       # 导入操作系统接口模块，用于路径和目录操作

# ==================== 数据库初始化 ====================

# 数据库文件存放目录名
dir_path = "data"
# 拼接得到完整的数据库文件路径
db_path = os.path.join(dir_path, "data.db")

# 检查 data 目录是否存在，不存在则创建
if not os.path.exists(dir_path):
    os.mkdir(dir_path)            # 创建文件夹
    print("已创建文件夹")
else:
    print("目录已存在，跳过创建文件夹")

# 连接 SQLite 数据库（如果文件不存在会自动创建）
data_base = sqlite3.connect(db_path)
# 创建游标对象，用于执行 SQL 语句
cursor = data_base.cursor()

# 定义建表 SQL：创建一个名为 test 的学生信息表
# sid     — 学号，整数型主键（唯一标识每一行）
# s_name  — 姓名，文本类型，不允许为空
# age     — 年龄，整数型
# sex     — 性别，文本型
# major   — 专业，文本型
sql_table = """CREATE TABLE IF NOT EXISTS test (
                sid INTEGER PRIMARY KEY,
                s_name TEXT NOT NULL,
                age INTEGER,
                sex TEXT,
                major TEXT
               )"""

try:
    # 执行建表语句
    cursor.execute(sql_table)
    # 提交事务，使更改生效
    data_base.commit()
    print("表创建成功！")
except Exception as e:
    # 如果建表出错，打印错误信息并回滚事务
    print(f"出错了：{e}")
    data_base.rollback()
finally:
    # 无论成功或失败，最后都关闭数据库连接释放资源
    data_base.close()
    print("数据库连接已关闭")