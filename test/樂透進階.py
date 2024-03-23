import random
num=list(random.sample(range(1,51),7))
#.sample=>隨機選取不重複的元素
special=num.pop()
print(f"樂透號:{sorted(num)}")
print(f"特別號:{special}")
