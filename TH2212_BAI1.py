d=float(input("Nhập chiều dài: "))
r=float(input("Nhập chiều rộng: "))
while True :
    if (d>=0) and (d<=100):
        break
    else:
        print("lỗi,nhập lại")
    if r>=0 and r<=100 :
        break
    else:
        print("lỗi, yêu cầu nhập lại")
c=(d+r)*2
s=d*r
print(f"chu vi hcn là: {c:.2f}")
print(f"diện tích hcn là : {s:.2f}")
