toan=float(input("nhập điểm toán: "))
ly=float(input("nhập điểm lý:"))
hoa=float(input("nhập điểm hóa:"))
tong=(toan+ly+hoa)
if tong>=15 and toan>=4 and ly>=4 and hoa>=4:
    print("đậu")
    if toan>=5 and ly>= 5 and hoa >= 5:
        print("học đều tất cả các môn")
    else:
        print("học chưa đều tất cả các môn")
else:
    print("thi hỏng")