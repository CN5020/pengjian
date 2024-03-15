import tkinter as tk  
from tkinter import messagebox  
  
class GearCalculator:  
    def __init__(self, master):  
        self.master = master  
        master.title("齿轮参数计算器")  
        master.geometry("400x300")  
  
        self.label_a = tk.Label(master, text="齿数：")  
        self.label_a.place(x=10, y=30)  
        self.teeth_a = tk.Entry(master)  
        self.teeth_a.place(x=100, y=30)  
  
        self.label_b = tk.Label(master, text="模数：")  
        self.label_b.place(x=10, y=60)  
        self.module_b = tk.Entry(master)  
        self.module_b.place(x=100, y=60)  
  
        self.label_c = tk.Label(master, text="压力角：")  
        self.label_c.place(x=10, y=90)  
        self.pressure_angle_c = tk.Entry(master)  
        self.pressure_angle_c.place(x=100, y=90)  
  
        self.label_d = tk.Label(master, text="螺旋角：")  
        self.label_d.place(x=10, y=120)  
        self.helix_angle_d = tk.Entry(master)  
        self.helix_angle_d.place(x=100, y=120)  
  
        self.calculate_button = tk.Button(master, text="计算", command=self.calculate)  
        self.calculate_button.place(x=150, y=150)  
  
        self.result_label = tk.Label(master, text="结果：")  
        self.result_label.place(x=10, y=220)  
        self.result = tk.StringVar()  
        self.result_display = tk.Label(master, textvariable=self.result)  
        self.result_display.place(x=150, y=220)  
  
    def calculate(self):  
        try:  
            teeth_a = float(self.teeth_a.get())  
            module_b = float(self.module_b.get())  
            pressure_angle_c = float(self.pressure_angle_c.get())  
            helix_angle_d = float(self.helix_angle_d.get())  
            # 在这里添加计算各种齿轮参数的逻辑，例如：模数、齿数、压力角、螺旋角等。  
            # 假设我们简单地将输入的模数和齿数相乘作为结果。  
            result = module_b * teeth_a  
            self.result.set("结果: " + str(result))  
        except ValueError:  
            messagebox.showerror("错误", "请输入正确的参数值。")  
  
root = tk.Tk()  
app = GearCalculator(root)  
root.mainloop()
