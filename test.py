import csv
import json 

# File CSV (Comma Separated Values)
# def csv_learn():                      
#     csv.


def json_learn():
        
    student = {                             # Dictionary        
        "name" : "quan",
        "age" : "19"
    }

    results = [                             # List[dictionary]
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

    with open("test.json", mode = 'w') as file:   
        json.dump(data, file, indent = 4)
# 1 file JSON chỉ chấp nhận 1 đối tượng JSON hợp lệ
# JSON chỉ cho phép 1 cấu trúc chính ( 1 object {} hoặc 1 array [])
# Nếu ghi json.dump() 2 lần, nó sẽ ghi 2 đối tượng k kết nối vào cùng 1 tệp -> gây ra tệp JSON k hợp lệ


if __name__ == '__main__':
    json_learn()