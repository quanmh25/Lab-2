
import csv
import json
import random

# Task 1:
def task_1():
    with open("books-en.csv", mode = 'r') as file:
        count = 0
        for line in file:
            tmp = list(line.split(';'))
            if len(tmp[1]) > 30:
                count += 1
        if count != 0:
            print("a) Количество записей с названием длиннее 30 символов:", count)
        else:
            print("Не найдено")
    
# Task 2:
def task_2():
    while True:
        author = input("Enter name of author: ")
        # To stop loop
        if author == 'quit':             
            break
        # Reset value of "cnt"
        cnt = 0 

        with open("books-en.csv", mode = 'r') as csv_file:
            for line in csv_file:
                row = list(line.split(';'))
                tmp = row[2].lower()
                res_find = tmp.find(author.lower())

                if res_find != -1 and float(row[3]) <= 2016:
                    cnt += 1
                    print(row) 

        if cnt != 0:
            print("b) Количество записей: ", cnt)        
        else:
            print("Не найдено")

       
def task_3():
    with open("result.txt", mode = 'w') as new_file:
        with open("books-en.csv", mode= 'r') as old_file:
            # Split the file into lines, each line is a list
            tmp = list(csv.reader(old_file, delimiter = ';'))
            for i in range(20):
                # Randomly select 1 line to write into txt file
                row = random.choice(tmp)
                if len(row) >= 4:
                    new_file.write(str(i + 1) +" " + str(row[2]) +'.'+ str(row[1]) + '-' + str(row[3]) + '\n')
            print("c) Написано")
    
# Extensible Markup Language

if __name__ == '__main__':
    task_1()
    task_2()
    task_3()


# Random.choice chỉ hoạt động với List và các kiểu dữ liệu có thứ tự: string, tuple
# Không hoạt động với từ điển Dict