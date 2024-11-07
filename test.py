import csv          # Nếu muốn mở csv.py để xem trong Module CSV có gì thì Ấn Ctrl và click chuột
import json 


# File CSV (Comma Separated Values)
def csv_learn():                      
    with open("memes_dataset.csv", mode = 'r', encoding = "utf8") as file:
        # file.readlines()                     # in ra chậm hơn dùng for 
        # for line in file:
        #     print(line.strip())              # nếu chỉ print(line) nó sẽ in ra 1 khoảng trắng (tức là xuống dòng 2 lần)

        csv_file = csv.DictReader(file)        # Đọc từng dòng của tệp csv sau đó chuyển đổi nó thành object dictionary 
        lst = list(csv_file)                   # list(dictionary) 
    # In kiểu này xấu, khó nhìn   
        print(lst)                            
    
    # Dùng json để in ra định dạng đẹp
        print(json.dumps(lst, indent = 4))

# Write CSV file:
    header = ["id", "name", "age", "mark"]
    students = ["407882", "quan", "19", "10"]

    with open("test.csv", mode = 'w', newline = '') as write_file:         # Nếu k ghi newline = '', nó sẽ mặc định tự hiểu là newline = '\n' và sẽ tự xuống dòng
        tmp = csv.writer(write_file)
        tmp.writerow(header)
        tmp.writerow(students)



def json_learn():

# Read JSON file
    with open("out.json", mode = 'r') as json_file:
        tmp = json.load(json_file)             # Đọc toàn bộ file JSON, sau đó chuyển nó thành đối tượng trong Python: List hoặc dictionary
        print(json.dumps(tmp, indent = 4))     # Chuyển đổi tmp trở lại chuỗi JSON (string), với thụt lề 4 khoảng trắng 

# Write JSON file      
    student = {                                # Dictionary        
        "name" : "quan",
        "age" : "19"
    }

    results = [                                # List[dictionary]
        {
            "name" : "quan",
            "mark" : "10"
        },
        {
            "name" : "anh",
            "mark" : "9"
        }
    ]

    # Gộp cả 2 vào 1 cấu trúc JSON hợp lệ
    data = {                                
        "student" : student,
        "results" : results
    }

    with open("test.json", mode = 'w') as write_file:   
        json.dump(data, write_file, indent = 4)
# 1 file JSON chỉ chấp nhận 1 đối tượng JSON hợp lệ
# JSON chỉ cho phép 1 cấu trúc chính ( 1 object {} hoặc 1 array [])
# Nếu ghi json.dump() 2 lần, nó sẽ ghi 2 đối tượng k kết nối vào cùng 1 tệp -> gây ra tệp JSON k hợp lệ



if __name__ == '__main__':
    # json_learn()
    csv_learn()