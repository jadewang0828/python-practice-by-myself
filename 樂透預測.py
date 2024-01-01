import random   #匯入亂數模組

lottoList=list()   #建立清單
for i in range(7):    #執行7次迴圈
    temp=random.randint(1, 49)      #temp=產生亂數1~49
    while temp in lottoList:       #如果temp產生的亂數有在49內且不重複
        temp=random.randint(1, 49)   #繼續產生亂數
    lottoList.append(temp)           #新增到清單內
    
special=lottoList.pop()            #移除最後一個數字並丟給special
print("樂透中獎號:",sorted(lottoList))   
print("特別號:",special)