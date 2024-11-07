from csv import reader

search = input("Nhap vao:")

flag = 0
with open("civic.csv", 'r') as file:
    table = reader(file, delimiter = ';')
    
    for i in table:
        print(i[3])
        lower_case = i[2].lower()
        index = lower_case.find(search.lower())   

        if index != 1:
            flag += 1
