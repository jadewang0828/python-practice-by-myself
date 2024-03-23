def addition(x=10,y=20):
    return f"預設1:{x},預設2:{y},相乘:{x}X{y}={x*y}"
a=int(input("請輸入第一個整數:"))
b=int(input("請輸入第二個整數:"))
print(addition())
print(f"您輸入的為:{addition(a,b)}")
print(f"交換後:{addition(y=a,x=b)}")
print(f"第一個整數 X 預設2:{addition(x=a,)}")
print(f"第二個整數 X 預設2:{addition(x=b,)}")
print(f"預設1 X 第一個整數:{addition(y=a)}")
print(f"預設1 X 第二個整數:{addition(y=b)}")
