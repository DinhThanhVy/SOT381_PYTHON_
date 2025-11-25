so_luong=[15,8,22,5,12,3]
ten_san_pham=["áo","quần","giày","túi","mũ","ví"]
print("các sản phẩm cần nhập thêm (số lượng<10):")
for i in range(len(so_luong)):
    if so_luong[i]<10:
        print(f"{ten_san_pham[i]}:{so_luong[i]}")