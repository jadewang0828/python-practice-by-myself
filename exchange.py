
with open(file="./ExchangeRate@202403131920.txt",mode="r",encoding="utf-8")as f:
    a=f.read()
    print(a)
money=input("請輸入幣別(ex:USD or HKD):")
buy=eval(input("請輸入買入價:"))

幣別=["USD","HKD","GBP","AUD","CAD"]
本行買入=[31.06, 3.866, 39.05, 20.41, 22.83]
本行賣出=[31.73,4.07,41.21,21.2,23.74]
for k,b,s in zip(幣別, 本行買入, 本行賣出):
    print(f"幣別:{k},買入:{b},賣出:{s}")

while True:
    print(b)
    if buy in str(b):
        print(f"您輸入的賣出價為:{s}")
        break
    else:
        print("輸入錯誤")
        money=input("請輸入幣別:")
        buy=eval(input("請輸入買入價:"))
print(f"本行今日賣出價為:{本行賣出}")
