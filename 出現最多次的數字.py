list1=[]
list2=[]
for i in range(1,11):
    x=int(input(f"請輸入第{i}個數字:"))
    list1.append(x)
print(f"您輸入的數字為:{list1}")
for y in range(10):
    list2.append(list1.count(list1[y]))
print(f"分別出現次數為:{list2}")
print(f"經比對後,出現最多次的數字位在第{list2.index(max(list2))}個索引值")
print(f"出現最多次次數:{max(list2)}")
list3=list1[list2.index(max(list2))]
print(f"{list3}出現最多次,共出現{max(list2)}次")