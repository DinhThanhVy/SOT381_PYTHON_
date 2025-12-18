n=int(input("nhập số lượng phần tử: "))
a=[]

for i in range(n):
    tam=int(input(f"a[{i}]="))
    a.append(tam)
print(f"Danh sách vừa nhập là:{a}")

tong_all=sum(a)
print(f"tổng các phần tử trong ds = {tong_all}")