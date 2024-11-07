import csv
import json

with open("books-en.csv", mode = 'r') as csv_file:
    table = list(csv.reader(csv_file, delimiter = ';'))
    # table.pop(0)

    sole_publisher = set()
    for row in table[1:]:
        sole_publisher.add(row[4])
    
    lst = list(sole_publisher)
    print(json.dumps(list(lst), indent = 4))
    print("Number of sole Publisher: ", len(lst), '\n')


    p = []                                
    for row in table[1:]:
        cnt = int(row[5])
        name = row[1]
        # Convert the value of price to a float
        price = float(row[6].replace(',','.'))       
        # Packaging to create a single argument because a list doesn't accept 3 arguments at the same time            
        p.append((cnt, name, price))                            
    
    p.sort(key = lambda x: (x[0], x[2]), reverse = True)         # Sort in descending

    for i in range(20):
        print(f'{i+1}. {p[i]}')


