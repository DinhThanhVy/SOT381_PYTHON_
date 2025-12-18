n=int(input("nhập số lượng phần tử: "))
a=[]

for i in range(n):
    tam=int(input(f"a[{i}]="))
    a.append(tam)
print(f"Danh sách vừa nhập là:{a}")

so_chan=0
so_le=0

for so in a:
    if so%2==0:
        so_chan+=1
    else:
        so_le+=1
print(f"Số lượng số chẵn là : {so_chan}")
print(f"Số lượng số lẻ là : {so_le}")