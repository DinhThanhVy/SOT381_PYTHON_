ten=input("Nhập tên sinh viên: ")
toan=float(input("Nhập điểm toán :"))
ly=float(input("Nhập điểm lý :"))
hoa=float(input("Nhập điểm hóa :"))
#tính điểm trung bình
dtb=(toan+ly+hoa)/3
#xếp loại
if dtb>=8 :
    xep_loai="giỏi"
elif dtb>=6.5 :
    xep_loai="khá"
elif dtb>=5 :
    xep_loai="trung bình"
else:
    xep_loai="yếu"
#xuất kết quả
    print("Họ tên :",ten)
    print("Điểm toán:",toan)
    print("Điểm lý:",ly)
    print("Điểm hóa:",hóa)
    print("Điểm trung bình:",dtb)
    print("Xếp loại: ",xep_loai)