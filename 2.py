import cmath  
  
def solve_quadratic(a, b, c):  
    # 计算判别式  
    D = (b**2) - (4*a*c)  
    # 计算两个解  
    sol1 = (-b-cmath.sqrt(D))/(2*a)  
    sol2 = (-b+cmath.sqrt(D))/(2*a)  
    return sol1, sol2  
  
# 输入方程的系数  
a = float(input("请输入方程的a系数: "))  
b = float(input("请输入方程的b系数: "))  
c = float(input("请输入方程的c系数: "))  
  
# 计算并输出解  
sol1, sol2 = solve_quadratic(a, b, c)  
print("方程的解为: x1 = ", sol1, ", x2 = ", sol2)
