nhiet_do=float(input("Nhập nhiệt độ: "))
loai=input("Nhập loại ( C;F;K): ")
if loai== "C":
 F= nhiet_do*9/5+32
 K=nhiet_do+273.15
 print(f"{nhiet_do:.2f}độ C={F:.2f}độ F")
 print(f"{nhiet_do:.2f}độ C={K:.2f}độ K")
elif loai == "F":
     C= (nhiet_do_32)*5/9
     K= C+273.15
     print(f"{nhiet_do:.2f}độ F={C:.2f}độ C")
     print(f"{nhiet_do:.2f}độ F={K:.2f}độ K")
elif loai == "K":
    C=nhiet_do-273.15
    F=C*9/5+32
    print(f"{nhiet_do:.2f}độ K={C:.2f}độ C")
    print(f"{nhiet_do:.2f}độ K={F:.2f}độ F")
else:
    print("Loại nhiệt độ không hợp lệ!")