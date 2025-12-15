n=int(input("nhập số n :"))
tong=0
for i in range(1,n+1):
    if n % 3==0 and n%2==0 :
        tong+=i
        print(f"tong={tong}")
    else:
        print("lỗi")