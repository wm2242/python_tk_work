import tkinter as tk
import time
import random

COLOR_FG = ['#00ff1a', '#00ffc4', '#f6ff00', '#ffa2d8', '#8f8fd4']
COLOR_BG = ['#0c1749', '#2a512e', '#956d37', '#686858', '#ca1f00']
INIT_VELOCITY = [-5, -4, -3, 3, 4, 5]
MOVE_INTERVAL = 200
LIGHT_STEP_INTERVAL = 200
LIGHT_STEP_COUNT = 15

class DynamicClock:
    """动态时钟应用 - 显示移动的时间标签"""

    def __init__(self, root: tk.Tk) -> None:
        self.root = root

        # 直接初始化所有属性
        self.text = tk.Label(
            self.root,
            text="",
            fg="black",
            bg="white",
            font=("Consolas", 24)
        )
        self.text.pack()

        # 初始化窗口
        self.root.overrideredirect(True)
        self.root.wm_attributes('-topmost', True)
        self.root.resizable(width=False, height=False)

        # 初始化移动参数
        self.x = min(500, self.root.winfo_screenwidth() - 100)
        self.y = min(500, self.root.winfo_screenheight() - 50)
        self.vx = random.choice(INIT_VELOCITY)
        self.vy = random.choice(INIT_VELOCITY)
        self.is_moving = True
        self.is_lighting = False

        # 绑定事件
        self.root.bind("<Escape>", self.on_escape)
        self.root.bind("<space>", self.on_toggle_move)

    def on_escape(self, _event: tk.Event[tk.Widget]) -> None:
        """Esc 键 - 退出应用"""
        self.root.destroy()

    def on_toggle_move(self, _event: tk.Event[tk.Widget]) -> None:
        """空格键 - 暂停/恢复移动"""
        self.is_moving = not self.is_moving
        if self.is_moving:
            self.update_movement()

    def update_clock(self) -> None:
        """更新时间显示"""
        time_str = time.strftime("%H:%M:%S")
        self.text.config(text=time_str)
        self.root.after(1000, lambda: self.update_clock()) # type: ignore[reportCallIssue]

    def flash_light(self, count: int) -> None:
        """碰撞闪烁效果"""
        if self.is_lighting:
            return
        self.is_lighting = True

        def step(n: int = count) -> None:
            if n > 0:
                self.text.config(
                    bg=COLOR_BG[n % len(COLOR_BG)],
                    fg=COLOR_FG[n % len(COLOR_FG)]
                )
                self.root.after(LIGHT_STEP_INTERVAL, lambda: step(n - 1)) # type: ignore[reportCallIssue]
            else:
                self.text.config(fg='black', bg='white')
                self.is_lighting = False

        step(count)

    def update_movement(self) -> None:
        """更新窗口位置和处理碰撞"""
        if not self.is_moving:
            return

        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        window_width = self.root.winfo_width()
        window_height = self.root.winfo_height()

        collided = False

        # 检查水平边界
        if self.x + window_width >= screen_width:
            self.x = screen_width - window_width
            self.vx = -self.vx
            collided = True
        elif self.x <= 0:
            self.x = 0
            self.vx = -self.vx
            collided = True

        # 检查垂直边界
        if self.y + window_height >= screen_height:
            self.y = screen_height - window_height
            self.vy = -self.vy
            collided = True
        elif self.y <= 0:
            self.y = 0
            self.vy = -self.vy
            collided = True

        if collided:
            self.flash_light(LIGHT_STEP_COUNT)

        # 移动
        self.x += self.vx
        self.y += self.vy
        self.root.geometry(f"+{self.x}+{self.y}")

        # 继续移动循环
        if self.is_moving:
            self.root.after(MOVE_INTERVAL, lambda: self.update_movement()) # type: ignore[reportCallIssue]

    def run(self) -> None:
        """启动应用"""
        self.update_clock()
        self.update_movement()
        self.root.mainloop()


def main() -> None:
    """主函数"""
    root = tk.Tk()
    app = DynamicClock(root)
    app.run()


if __name__ == "__main__":
    main()