while True:
    n=int(input("Nhập số n :"))
    if n >=0 and n<=10 :
        giai_thua=1
        for i in range(1,n+1):
            giai_thua*=i
        print(f"{n}={giai_thua}")
        break
    else:
        print("Nhập lại số hợp lệ")