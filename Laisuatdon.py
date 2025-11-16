so_tien_gui=float(input("Nhập số tiền gửi:"))
lai_suat=float(input("Nhập lãi suất (%/năm): "))
so_thang=int(input("Nhập số tháng gửi:"))
#tính tiền lãi
lai=(so_tien_gui*lai_suat*so_thang)/12/100
print("Tiền lãi nhận được là:",round(lai,2))