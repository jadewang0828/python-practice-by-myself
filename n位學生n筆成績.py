a=[]
b=[]
for i in range(3):
    c=input(f"請輸入第{i+1}位學生:")
    a.append(c)
    for x in range(5):
        d=eval(input(f"請輸入第{i+1}位學生的第{x+1}筆成績:"))
        b.append(d)    
e=a[0],b[0:5]
f=a[1],b[5:10]
g=a[2],b[10:]
print(f"第一位學生:{e}")
print(f"第二位學生:{f}")
print(f"第三位學生:{g}")
h=list(b[0:5])
i=list(b[5:10])
j=list(b[10:])
k=sum(h)/5
l=sum(i)/5
m=sum(j)/5
print(f"第一位學生的總分為:{sum(h)}, 平均分數為:{k:.2f}")
print(f"第二位學生的總分為:{sum(i)}, 平均分數為:{l:.2f}")
print(f"第三位學生的總分為:{sum(j)}, 平均分數為:{m:.2f}")
