
# Вариант 2: До 2016 года

import csv
import json


# Task 1:
def task_1():
    with open("books-en.csv", mode = 'r') as file:
        cnt = 0

        # lst = list(csv.DictReader(file, delimiter = ';'))
        # for line in lst:
        #     if len(line['Book-Title']) >= 30:
        #         cnt += 1
      
        for line in file:
            tmp = list(line.split(';'))
            if len(tmp[1]) >= 30:
                cnt += 1
        print(cnt)

    

if __name__ == '__main__':
    task_1()