a=int(input("請輸入第一個整數:"))
b=int(input("請輸入第二個整數:"))
cod=input("請樹入運算子(+、-、*、//、/、%、**):")

if cod=="+":
    print(f"{a}+{b}={a+b}")
elif cod=="-":
    print(f"{a}-{b}={a-b}")
elif cod=="*":
    print(f"{a}*{b}={a*b}")
elif cod=="//":
    if b==0 :print("除數不可為0")
    else:print(f"{a}//{b}={a//b}")
elif cod=="/":
    if b==0 :print("除數不可為0")
    else:print(f"{a}/{b}={a/b}")
elif cod=="%":
    if b==0 :print("除數不可為0")
    else:print(f"{a}%{b}={a%b}")
elif cod=="**":
    print(f"{a}**{b}={a**b}")
else:
    print("無法識別")
        