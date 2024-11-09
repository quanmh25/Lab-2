# Practical lesson on Tue 08.10.24

import csv
import json


# Đường dẫn đến file
DATASET_PATH = "memes_dataset.csv"              
OUT_PATH = "out.json"

# Lấy tiêu đề của file csv
def get_title(dataset):                   
    dataset.seek(0)                                     # Đặt con trỏ về đầu tệp, để chắc chắn đọc từ đầu 
    title = next(dataset)                               # Lấy dòng đầu tiên của file và cũng là tiêu đề                     
    title = title.split(",")                            # Xét 1 dòng, sau đó tách các phần tử bị ngăn cách bởi dấu phẩy thành các cột
    # title = list(title.split(","))                    # Khi gọi title.split() nó sẽ tự động trả về list nên k cần gán list ở đầu
                                                        # title lúc này đang là list
    title = [col.strip() for col in title]              # List comprehension để xóa bỏ khoảng trống ở đầu và cuỗi của mỗi tên cột trong title

    # title = [col.strip() for col in title.split(",")]       #Lệnh này có thể thay thế cho dòng 14 và 17 
    return title


# Lấy 1 đối tượng từ 1 dòng dữ liệu Line trong csv và trả về dưới dạng dictionary
def get_object_alt(line, title): 
    # [line] biến line thành 1 list chỉ chứa 1 phần tử là dòng dữ liệu
    # delimiter chỉ định dấu phẩy là ký tự phân cách giữa các tường
    # quotechar chỉ định dấu " dùng để bao quanh các giá trị
    
    reader = csv.DictReader([line], title, delimiter=',', quotechar='"')         
    result = next(reader)                                # Lấy đối tượng đầu tiên từ reader
    return result


def get_object(line, title):
    fields = []
    value = ""                               # Chuỗi rỗng
    in_complex = False

    for char in line:                        # Mỗi lần lặp các ký tự trong line sẽ được gắn vào biến char
        # nếu đang ở trong trường phức tạp các ký tự sẽ được tích lũy cho đến khi gặp dấu ngoặc kép đóng
        if in_complex:                
            value += char

            if char == '"':                  # Khi gặp dấu ngoặc kép đóng "
                value = value[:-1]           # Bỏ dấu ngoặc kép
                fields.append(value)             
                value = ''
                in_complex = False           # Đặt lại để thông báo rằng đã ra khỏi trường phức tạp
        else:
            if char not in (',', '"'):
                value += char
                continue
            
            if char == ',':
                fields.append(value)
                value = ''
                continue
            
            if char == '"':
                in_complex = True
                continue

    # Hàm sử dụng zip để ghép cặp tiêu đề với cột giá trị tương ứng, rồi trả về kết quả dưới dạng từ điển
    result = {col: f for col, f in zip(title, fields)}         
    return result


def filter_year(dataset, title, year):
    filtered = []

    for line in dataset:
        obj = get_object(line, title)
        year_value = obj["origin_year"]

        if year_value == str(year):
            filtered += [obj]

    dataset.seek(0)
    return filtered


if __name__ == "__main__":
    with open(DATASET_PATH, encoding="utf-8") as dataset:             # dataset đại diện cho file vừa mở
        title = get_title(dataset)

        res = filter_year(dataset, title, 1990)
        print(len(res))
        # for r in res:
        #     print(r)

        # line = next(dataset)
        # res = get_object_alt(line, title)

        # print(res)

        res = json.dumps(res, indent=4)
        with open(OUT_PATH, "w") as out:
            out.write(res)


# Trường phức tạp là gì? (complex field)
# Là trường dữ liệu được bao quanh bởi dấu ngoặc kép (""), những tường này chứa ký tự đặc biệt (có thể là dấu phẩy - dễ gây nhầm lẫn với dấu phẩy ngăn cách trong csv)