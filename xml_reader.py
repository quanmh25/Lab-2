import xml.dom.minidom as minidom


xml_file = open('books.xml', 'r')         
xml_data = xml_file.read()                           # Đọc nội dung file vào chuỗi

dom = minidom.parseString(xml_data)                  # Phân tích chuỗi XML thành đối tượng DOM
dom.normalize()                                      # Chuẩn hóa cấu trúc DOM để dễ xử lý

elements = dom.getElementsByTagName('book')          # Lấy các phần tử của book và trả về 1 Nodelist
books_dict = {}

for node in elements:
    for child in node.childNodes:
        if child.nodeType == 1:                                                       # Ktra nếu là 1 element node
            if child.tagName == 'title':
                if child.firstChild.nodeType == 3:                                # Nếu có ndung văn bản
                    title = child.firstChild.data                                 # Lấy dữ liệu văn bản của ptu <title> và gán cho biến title
            if child.tagName == 'price':
                if child.firstChild.nodeType == 3:
                    price = float(child.firstChild.data)                          # Gán dữ liệu của <price> cho price
    books_dict[title] = price                                                     # Thêm tiêu đề price vào book_dict

    # Tìm sách với thuộc tính id="bk106" và in tiêu đề của nó
    if node.getAttribute('id') == 'bk106':
        print(node.getElementsByTagName('title')[0].firstChild.data)

#for key in books_dict.keys():
    #print(key, books_dict[key])

print(books_dict)


xml_file.close()
