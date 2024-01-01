sex=input("你的性別是(男/女):")
hight=eval(input("你的身高(cm)是:"))
weight=eval(input("你的體重(kg)是:"))
bmi=weight/(hight/100)**2
boySampleWeight=(hight-80)*0.7
girlSampleWeight=(hight-70)*0.6
if sex=="男":
    if bmi>25:
        print("體重過重")
    elif bmi<20:
        print("體重過輕")
    else:
        print("身材適中")
    print(f"建議體重為:{boySampleWeight:.2f}")
else:
    if bmi>22:
        print("體重過重")
    elif bmi<18:
        print("體重過輕")
    else:
        print("身材適中")
    print(f"建議體重為:{girlSampleWeight:.2f}")