import math
a=float(input("Nhập cạnh thứ nhất (cm): "))
b=float(input("Nhập cạnh thứ hai (cm): "))
c=float(input("Nhập cạnh thứ ba (cm): "))
C=a+b+c
p=(a+b+c)/2
s=math.sqrt(p*(p-a)*(p-b)*(p-c))
print(f"chu vi hình tam giác là :{C:.2f}")
print(f"diện tích hình tam giác là :{s:.2f}")