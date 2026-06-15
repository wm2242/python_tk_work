import tkinter as tk

def perform_operation(operation):
    try:
        num1 = float(text1.get())
        num2 = float(text2.get())

        if operation == '+':
            result_value = num1 + num2
            result.insert(tk.END, f'{num1} + {num2} = {result_value}\n')
        elif operation == '-':
            result_value = num1 - num2
            result.insert(tk.END, f'{num1} - {num2} = {result_value}\n')
        elif operation == '*':
            result_value = num1 * num2
            result.insert(tk.END, f'{num1} * {num2} = {result_value}\n')
        elif operation == '/':
            if num2 == 0:
                result.insert(tk.END, "错误：除数不可为零\n")
            else:
                result_value = num1 / num2
                result.insert(tk.END, f'{num1} / {num2} = {result_value}\n')

        text1.delete(0, 'end')
        text2.delete(0, 'end')

    except ValueError:
        result.insert(tk.END, "错误：请输入有效的数字\n")
        text1.delete(0, 'end')
        text2.delete(0, 'end')

def clear_all():
    text1.delete(0, 'end')
    text2.delete(0, 'end')
    result.delete(1.0, tk.END)

root = tk.Tk()
root.title("简易计算器")
root.geometry("400x300")

tk.Label(root, text="第一个数:", font=("Arial", 10)).pack(pady=5)
text1 = tk.Entry(root, font=("Arial", 12), width=30)
text1.pack(pady=5)

tk.Label(root, text="第二个数:", font=("Arial", 10)).pack(pady=5)
text2 = tk.Entry(root, font=("Arial", 12), width=30)
text2.pack(pady=5)

button_frame = tk.Frame(root)
button_frame.pack(pady=10)

tk.Button(button_frame, text='加', command=lambda: perform_operation('+'),
          width=8, font=("Arial", 10)).grid(row=0, column=0, padx=5)
tk.Button(button_frame, text='减', command=lambda: perform_operation('-'),
          width=8, font=("Arial", 10)).grid(row=0, column=1, padx=5)
tk.Button(button_frame, text='乘', command=lambda: perform_operation('*'),
          width=8, font=("Arial", 10)).grid(row=0, column=2, padx=5)
tk.Button(button_frame, text='除', command=lambda: perform_operation('/'),
          width=8, font=("Arial", 10)).grid(row=0, column=3, padx=5)

tk.Button(button_frame, text='清除', command=clear_all,
          width=8, font=("Arial", 10)).grid(row=1, column=0, columnspan=4, pady=5, sticky="ew")

tk.Label(root, text="计算结果:", font=("Arial", 10)).pack(pady=5)
result = tk.Text(root, height=8, width=50, font=("Arial", 10))
result.pack(pady=5)

root.mainloop()