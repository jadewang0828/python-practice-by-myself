import csv
with open(file="./test.csv",mode="r",encoding="utf-8")as f:
    data=csv.reader(f)
    print(type(data))
    data_list=list(data)
    print(type(data_list))
    for i in data:
        print(i)
    print(data_list[0])