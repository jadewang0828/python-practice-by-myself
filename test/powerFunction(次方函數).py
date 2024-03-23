def power(x,y):
    return x**y
    
x=eval(input("請輸入底數數字:"))
y=eval(input("請輸入次方數字:"))
    
print(f"{x}的{y}次方為{power(x,y):.2f}")