score = 80
if score >= 81:
    print("及格")


 #   if 多分支判断
score1 = input ("请输入您的分数")
score1 = int(score1)
if score1 > 85:
    print("优秀")
elif score1 > 75:
    print ("良")
elif score1 > 60:
    print("及格")
else:
    print("不及格")
