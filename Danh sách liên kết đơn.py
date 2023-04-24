class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        # Đây là nút đầu tiên trong danh sách và khởi tạo bằng giá trị None
        self.head = None
# Hàm thêm phần tử
    def add_node(self, value):
        new_node = Node(value)
        # Nếu danh sách rỗng nút mới sẽ được gán là nút đầu tiên của danh sách
        if self.head is None:
            self.head = new_node
        # Ngược lại nếu danh sách không rỗng nút hiện tại sẽ được xem là nút đầu tiên
        else:
            current_node = self.head
            # Sử dụng vòng lặp để kiểm tra nút tiếp theo của nút hiện tại có tồn tại hay không
            # nếu có nút hiện tại sẽ được coi là nút tiếp theo
            # và nút tiếp theo được coi là nốt mới 
            while current_node.next is not None:
                current_node = current_node.next
            current_node.next = new_node
# Hàm in danh sách
    def print_list(self):
        # Gán nốt hiện tại là nốt đầu tiên của danh sách
        current_node = self.head
        # Kiểm tra nếu nốt hiện tại không rỗng thì in giá trị nốt hiện tại và gán cho nốt tiếp theo và nốt đó được xem là nốt hiện tại
        # và thực hiện vòng lặp cho đến khi nốt hiện tại là nốt rỗng
        while current_node is not None:
            print(current_node.value)
            current_node = current_node.next
# Hàm duyệt danh sách
    def traverse_list(self):
        # Gán nốt hiện tại cho nốt đầu tiên của danh sách
        current_node = self.head
        # Gán index = 0 vì trong danh sách liên kết phần tử đầu tiên được đánh số là 0
        index = 0
        print("Các phần tử trong danh sách: ")
        # Kiểm tra nốt hiện tại, nếu không rỗng thì in vị trí và giá trị của nốt hiện tại ra màn hình
        # Sau đó gán nốt hiện tại cho nốt tiếp theo và nốt tiếp theo đó lúc bây giờ sẽ được xem là nốt hiện tại
        # Và biến index sẽ tăng thêm một đơn vị
        # vòng lặp sẽ kết thúc khi nốt hiện tại có giá trị rỗng
        while current_node is not None:
            print("Vị trí:", index, "Giá trị:", current_node.value)
            current_node = current_node.next
            index += 1
# Hàm xóa phần tử
    def remove_node(self, value):
            # Gán nốt hiện tại cho nốt đầu tiên của danh sách
            current_node = self.head
            # Gán nốt trước là rỗng
            previous_node = None
            count = 0
            while current_node is not None:
                # Nếu giá trị nốt hiện tại bằng với giá trị ta cần xóa thì ta xóa nốt đó
                if current_node.value == value:
                    if previous_node is None:
                        self.head = current_node.next
                    else:
                        previous_node.next = current_node.next
                    return True
                else:
                    previous_node = current_node
                    current_node = current_node.next
            return False

# Hàm tìm kiếm phần tử
    def search_node(self, value):
        current_node = self.head
        index = 0
        count = 0
        while current_node is not None:
            # Nếu giá trị nốt hiện tại bằng giá trị ta cần tìm thì in ra vị trí và giá trị đó, rồi đếm giá trị đó lần đầu tiên
            if current_node.value == value:
                print("Phần tử có giá trị", value, "được tìm thấy tại vị trí", index)
                count += 1
            # Gán nốt hiện tại cho nốt tiếp theo và tăng vị trí đó lên 1 đơn vị
            current_node = current_node.next
            index += 1
        # nếu không đếm được giá trị đó lần nào thì sẽ in ra kết quả không tìm thấy
        if count == 0:
            print("Không tìm thấy phần tử có giá trị", value)
            return False
        # Nếu đếm được một lần thì đó là giá trị duy nhất trong danh sách
        elif count == 1:
            return True
        # Nếu giá trị xuất hiện 2 lần hoặc hơn thì in ra phần tử đó là số lần xuất hiện của phần tử đó
        else:
            print("Phần tử có giá trị", value, "xuất hiện", count, "lần trong danh sách")
            return True

my_list = LinkedList()
# thực thi thêm các phần tử trong danh sách
while True:
    values = input("Nhập các giá trị cần thêm, cách nhau bởi dấu cách, hoặc gõ End để kết thúc: ")
    if values == "End":
        break
    for value in values.split():
        my_list.add_node(int(value))

# Thực thi Xóa các phần tử trong danh sách
print("****Danh sách trước khi xóa****")
my_list.traverse_list()

while True:
    values = input("Nhập các giá trị cần xóa, cách nhau bởi dấu cách, hoặc gõ End để kết thúc: ")
    if values == "End":
        break
    for value in values.split():      
        my_list.remove_node(int(value))

# Thực thi kiểm tra việc xóa phần tử
print("****Danh sách sau khi xóa****")
my_list.traverse_list()

# Thực thi kiểm tra việc tìm kiếm phần tử
while True:
    values = input("Nhập các giá trị cần tìm kiếm, cách nhau bởi dấu cách, hoặc gõ End để kết thúc: ")
    if values == "End":
        break
    for value in values.split():
        my_list.search_node(int(value))


