import tkinter as tk
import random
def main():
    vx = random.randint(1,10)
    vy = random.randint(1,10)
    def run():
        nonlocal vx, vy
        if lab.winfo_width() + lab.winfo_x() > root.winfo_width():
            lab.place(x = root.winfo_width() - lab.winfo_width())
            vx = -vx
        if lab.winfo_x() < 0:
            lab.place(x = 0)
            vx = -vx
        if lab.winfo_y() + lab.winfo_height() > root.winfo_height():
            lab.place(y = root.winfo_height() - lab.winfo_height())
            vy = -vy
        if lab.winfo_y() < 0:
            lab.place(y = 0)
            vy = -vy
        lab.place(x = lab.winfo_x() + vx, y = lab.winfo_y() + vy)
        root.after(50, run) # type: ignore[reportCallIssue]
    root = tk.Tk()
    root.geometry("400x300")
    lab = tk.Label(root, text="Hello World")
    lab.place(x=200, y=150)
    run()
    root.mainloop()

if __name__ == "__main__":
    main()