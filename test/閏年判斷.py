year=int(input("請輸入一個西元年年份:"))
#閏年:每 4 年一閏、遇 100 年不閏、遇 400 年要閏

if year%400 ==0:
    print(f"{year}年是閏年。")
elif year%100==0:
    print(f"{year}年不是閏年。")
elif year%4==0:
    print(f"{year}年是閏年。")
else:
    print(f"{year}年不是閏年。")