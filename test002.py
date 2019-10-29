# 键盘输入利润
totalProfit = int(input('请输入 利润：'))

# 利润区间对应的 提成比例 依次计算

result = 0
# 计算10万元部分
if totalProfit - 10 * 10000 > 0:
    totalProfit -= 10 * 10000
    result+=10*10000*0.1
else:
    result+=totalProfit*0.1
    print(result * 0.1)
    exit(0)
# 计算10~20 万元的部分

if totalProfit - 10*10000>0:
    totalProfit-=10*10000
    result+=10*10000*0.075
else:
    result+=totalProfit*0.075
    print(result)
    exit(0)

# 计算20~40 万元的部分

if totalProfit - 20*10000>0:
    totalProfit-=20*10000
    result+=20*10000*0.05
else:
    result+=totalProfit*0.05
    print(result)
    exit(0)

# 计算40~60 万元的部分

if totalProfit - 20*10000>0:
    totalProfit-=20*10000
    result+=20*10000*0.03
else:
    result+=totalProfit*0.03
    print(result)
    exit(0)

# 计算60~100 万元的部分

if totalProfit - 40*10000>0:
    totalProfit-=40*10000
    result+=40*10000*0.015
else:
    result+=totalProfit*0.015
    print(result)
    exit(0)

# 计算10~20 万元的部分

if totalProfit - 100*10000>0:
    totalProfit-=100*10000
    result+=100*10000*0.01
print(result)