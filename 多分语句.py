# 王子建
# 开发时间：2023/8/11 21:38
'''
if 表达式1:
    语句1
    语句
    语句
elif 表达是2:
else 表达是：
'''
print("*"*80)
print("接下来计算您的bmi")
print("*"*80)
high=float(input("请输入您的身高（m）："))
weight=int(input("请输入您的体重（kg）："))
bmi=weight/high**2
print(round(bmi))
if bmi<18.5:
    print("偏瘦")
elif 18.5<bmi<24:
    print("正常")
elif 24<bmi<28:
    print("超重")
else :
    print('肥胖')
print("bmi测试结束，欢迎再次光临")