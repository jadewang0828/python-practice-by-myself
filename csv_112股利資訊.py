import csv
with open(file="./112年度股利.csv",mode="r")as f:
    csc_read=csv.reader(f)
    print(csc_read)
    csc_list=list(csc_read)
    for i in csc_list:
        print(i)
    print(csc_list[500])