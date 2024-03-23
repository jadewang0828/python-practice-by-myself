hight=eval(input("請輸入身高(cm):"))
weight=eval(input("請輸入體重(kg):"))
while hight!=1 and weight!=1:
    try:
        assert hight<=300,"身高超過300 cm" 
        assert weight<=200,"體重超過200 kg"
        bmi=weight/((hight/100)**2)
        print(f"您的bmi為:{bmi:.2f}")   
    except Exception as e:
        print("超過合理範圍!重新輸入",e)
    finally:
        hight=eval(input("請重新輸入身高(cm)或按 1 退出:"))
        weight=eval(input("請重新輸入體重(kg)或按 1 退出:"))