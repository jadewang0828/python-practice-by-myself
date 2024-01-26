week={
      "日":"Sunday",
      "一":"Monday",
      }
find=input("請輸入要搜尋的日期:")
if find in week:
    print("find the keys")
elif find in week.values():
    print("find the values")
else:
     print("not found")   