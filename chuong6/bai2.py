def hieu(mang_a, mang_b):
    # Dùng set để loại bỏ các phần tử trùng nhau và dễ dàng tìm hiệu
    tap_hop_a = set(mang_a)
    tap_hop_b = set(mang_b)
    
    # Tìm các phần tử có trong a nhưng không có trong b
    tap_hop_c = tap_hop_a - tap_hop_b
    
    # Chuyển set thành list và sắp xếp theo thứ tự tăng dần
    mang_c = sorted(list(tap_hop_c))
    
    return mang_c

# Ví dụ
mang_a = [1, 5, 3, 7, 9, 4, 2]
mang_b = [9, 6, 2, 3, 8]
mang_c = hieu(mang_a, mang_b)
print(mang_c)  # Output: [1, 4, 5, 7]
