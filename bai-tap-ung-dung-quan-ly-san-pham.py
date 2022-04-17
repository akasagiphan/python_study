#!/usr/bin/env python
# coding: utf-8

# In[39]:


product_list = {}
exit = False

def product_lookup(product_list,id):
    if id in product_list.keys():
        return product_list[id]
    else:
        return None

def product_update(product_list,id,name):
    product_list[id] = name
    
def product_remove(product_list,id):
    del product_list[id]

print("Danh sách sản phẩm ban đầu:",product_list)
print("----------------------------")

while exit == False:
    exit_check = str(input("Bạn có muốn thay đổi danh sách sản phẩm? (y/n): "))
    
    while exit_check not in ("y","n"):
        exit_check = str(input("Sai cú pháp! Vui lòng chỉ chọn y hoặc n: "))
    print("----------------------------")
    
    if exit_check == "n":
        print("Chương trình kết thúc.")
        print("Danh sách sản phẩm cuối cùng:",product_list)
        exit = True
    
    else:
        print("Vui lòng nhập lựa chọn xử lý:\n1-Thêm sp\n2-Cập nhật sp\n3-Xóa sản phẩm\n4-Thoát chương trình")
        option = str(input("Nhập lựa chọn của bạn (1/2/3/4): "))
        
        while option not in ("1","2","3","4"):
            option = str(input("Sai cú pháp! Nhập lựa chọn của bạn (1/2/3/4): "))
        option = int(option)
        print("----------------------------")
        
        if option == 1: # Add
            print("Bạn đã chọn thêm sản phẩm.")
            id = input("Nhập id sản phẩm muốn thêm: ")
            
            if product_lookup(product_list,id) != None:
                print("Sản phẩm đã tồn tại. Lệnh thêm không được thực thi!")
            
            else:
                name = str(input("Nhập tên sản phẩm: "))
                product_update(product_list,id,name)
            
            print("----------------------------")
            print("Danh sách sản phẩm hiện tại:",product_list)
            print("----------------------------")
        
        elif option == 2: # Update
            print("Bạn đã chọn cập nhật sản phẩm đang có.")
            id = input("Nhập id sản phẩm muốn cập nhật: ")
            
            if product_lookup(product_list,id) != None:
                name = str(input("Nhập tên sản phẩm: "))
                product_update(product_list,id,name)
            
            else:
                print("Sản phẩm không tồn tại. Lệnh cập nhật không được thực thi!")
            
            print("----------------------------")
            print("Danh sách sản phẩm hiện tại:",product_list)
            print("----------------------------")
        
        elif option == 3: # Remove
            print("Bạn đã chọn xóa sản phẩm đang có.")
            id = input("Nhập id sản phẩm muốn loại ra: ")
            
            if product_lookup(product_list,id) != None:
                product_remove(product_list,id)
            
            else:
                print("Sản phẩm không tồn tại. Lệnh xóa không được thực thi!")
            
            print("----------------------------")
            print("Danh sách sản phẩm hiện tại:",product_list)
            print("----------------------------")
        
        elif option == 4:
            print("Chương trình kết thúc.")
            print("Danh sách sản phẩm cuối cùng:",product_list)
            break

