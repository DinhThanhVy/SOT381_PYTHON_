d=float(input("Nhập chiều dài: "))
r=float(input("Nhập chiều rộng: "))
while d>=0.0 and r<=100.0:
 c=(d+r)*2
 s=d*r
 print(f"chu vi hcn là:{c:.2f}")
 print(f"diện tích hcn là:{s:.2f}")
 break