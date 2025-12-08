n=10
tong_cac_so_le=0
print(f"Các số lẻ từ 1 đến {n} : ")

for i in range(1,n+1,2):
    tong_cac_so_le=tong_cac_so_le+i
    print(f"{i}")
    
print(f"tổng các số lẻ là : {tong_cac_so_le}")