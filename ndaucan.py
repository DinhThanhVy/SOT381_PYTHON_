import math
n=int(input("nhập số căn:"))
s=0
for i in range(1,n):
    s=math.sqrt(i+s)
    
print(f"tổng ={s:.3f}")