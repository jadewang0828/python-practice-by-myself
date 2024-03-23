import pandas as pd
import csv
x=pd.read_csv('全台藥品資料.csv',dtype='str')
註銷狀態=x['註銷狀態']
中文品名=x['中文品名']
result_dict={}
for i in range(len(註銷狀態)):
    key=註銷狀態[i]
    value=中文品名[i]
    if pd.isna(key):    #.isna => 檢查是否存在缺失值
        key= '無註銷'
#if pd.isna(key): key='無註銷' => 表示如果key存在缺失值, 就將缺失的名稱更改為'無註銷'
    if key not in result_dict:
        result_dict[key]=[]
    result_dict[key].append(value)
#如果自訂義的key名稱不在字典裡, 那就新增[key],順帶新增value
# print(result_dict)
with open('n22_clear.csv','w',encoding='utf-8')as csvfile:
    title=['註銷狀態', '中文品名']
    w=csv.DictWriter(csvfile, fieldnames=title)
    w.writeheader()
    for k,v in result_dict.items():
        for va in v:
            w.writerow({'註銷狀態': k, '中文品名': va})
print("CSV 檔案已成功寫入")
