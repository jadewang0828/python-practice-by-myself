def compute(x,y,sign):
    def add(x,y):
        x+y
        print(f"第一個整數{x}+第二個整數{y}=總和{x+y}")
    def sub(x,y):
        x-y
        print(f"第一個整數{x}-第二個整數{y}=總和{x-y}")
    def mul(x,y):
        x*y
        print(f"第一個整數{x} X 第二個整數{y}=總和{x*y}")
    def div(x,y):
        x/y
        print(f"第一個整數{x} ÷ 第二個整數{y}=總和{x/y}")
    if sign=="+":
        add(x, y)
    elif sign=="-":
        sub(x, y)
    elif sign=="*":
        mul(x, y)
    elif sign=="/":
        div(x, y)
while True:    
    x_a=float(input("請輸入第一個整數:"))
    y_b=float(input("請輸入第二個整數:"))
    sign_c=input("請輸入要運算的符號(+,-,*,/):")
    print(compute(x_a,y_b,sign_c))
    choice_=int(input("輸入0終止程式 / 輸入1繼續操作:"))
    if choice_==0:
        break
    print()
print("程式中止")