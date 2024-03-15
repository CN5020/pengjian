import tkinter as tk  
from tkinter import messagebox  
from sympy import symbols, Eq, solve  
  
def solve_quadratic_equation():  
    # 获取用户输入  
    a_value = float(a_entry.get())  
    b_value = float(b_entry.get())  
    c_value = float(c_entry.get())  
  
    # 检查输入是否有效  
    if a_value == 0:  
        messagebox.showerror("错误", "系数a不能为0！")  
        return  
  
    # 定义变量  
    x, y = symbols('x y')  
  
    # 建立方程组  
    equation1 = Eq(a*x + b*y, c)  
    equation2 = Eq(b*x - a*y, 0)  
  
    # 使用solve解方程组  
    solutions = solve((equation1, equation2), (x, y), dict=True)  
  
    # 显示结果  
    if solutions:  
        x_value = solutions[0][x]  
        y_value = solutions[0][y]  
        result_label.config(text="解为： x = " + str(x_value) + ", y = " + str(y_value))  
    else:  
        messagebox.showerror("错误", "无解或解不唯一！")  
  
# 创建主窗口  
root = tk.Tk()  
root.title("二元一次方程求解器")  
  
# 创建输入框和标签  
a_label = tk.Label(root, text="系数a:")  
a_label.pack()  
a_entry = tk.Entry(root)  
a_entry.pack()  
  
b_label = tk.Label(root, text="系数b:")  
b_label.pack()  
b_entry = tk.Entry(root)  
b_entry.pack()  
  
c_label = tk.Label(root, text="系数c:")  
c_label.pack()  
c_entry = tk.Entry(root)  
c_entry.pack()  
  
# 创建求解按钮  
solve_button = tk.Button(root, text="求解", command=solve_quadratic_equation)  
solve_button.pack()  
  
# 创建结果标签  
result_label = tk.Label(root, text="")  
result_label.pack()  
  
# 运行主循环  
root.mainloop()
