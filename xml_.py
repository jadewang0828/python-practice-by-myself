import xmltodict
with open("./53_1.xml",encoding="utf-8")as f:
    str_f=f.read()
    dict_f=xmltodict.parse(str_f)
    print(type(dict_f))
    list_f=dict_f["dataList"]
    dict_rows=list_f["rows"]
    panadol=dict_rows[0]
    print(panadol["藥理作用機轉"])
    drug_list=list()
    for i in dict_rows:
        list_title=list(i)
        drug=drug_list.append(i["藥品成分"])
print(drug_list)
