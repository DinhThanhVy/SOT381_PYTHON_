n=int(input("Nhập số nguyên: "))

s1=0
for i in range(1,n+1):
    s1=s1+1/(i*(i+1))
    
import math
s2=0
for i in range(1,n):
    s2=math.sqrt(3+s2)
    
print(f"s1={s1:.3f}")
print(f"s2={s2:.3f}")