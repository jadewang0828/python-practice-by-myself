a={"a","b","c","d","e","f"}
print(a)
print(type(a))
#for b in a:
#    c=str(b)
#    d=ord(c)
#    print("目前項目有:",c,d,sep=":")

list_a=list(a)
user_choice=input("請輸入要新增(add)或刪除(del):")
if user_choice == "add":
    user_add=str(input("請問要新增什麼項目?(int,str,bool,float):"))
    if user_add == "int":
        user_int=int(input("請輸入要新增的數字:"))
        list_a.append(user_int)
        print(list_a)
    elif user_add=="str":
        user_str=str(input("請輸入要新增的字母:"))
        list_a.append(user_str)
        print(list_a)
    elif user_add=="bool":
        user_bool=eval(input("請輸入要新增True或False:"))
        list_a.append(user_bool)
        print(list_a)
    elif user_add=="float":
        user_float=float(input("請輸入要新增的浮點數:"))
        list_a.append(user_float)
        print(list_a)
elif user_choice =="del":
    list_a=list(a)
    user_del=str(input("請問要刪除什麼項目?(int,str,bool,float):"))
    if user_del=="int":
        print("列表中無數字")
    elif user_del=="bool":
        print("列表中無布林值")
    elif user_del=="float":
        print("列表中無浮點數")
    elif user_del=="str":
        print(f"列表中有{a}")
        user_str=str(input("請輸入要刪除的字母:"))
        if user_str in list_a:
            list_a.remove(user_str)
        print(list_a)
    print()
