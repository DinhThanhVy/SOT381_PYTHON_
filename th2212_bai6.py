n=int(input("nhập số lượng bài hát yêu thích:"))
dsbh=[]
for i in range(n):
    ten=input("nhập tên bài hát thứ i:")
    dsbh.append(ten)
for i in range(n):
    ten=dsbh[i]
    print(f"bài thứ {i} : {ten}")
for i in dsbh:
    print("{bai}")