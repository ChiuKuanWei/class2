# for i in range(1,10):
#     print(f'i={i}')
#     print('j=',end='')   
#     for j in range(1,10):       
#         print(f'{j}',end=' ')
#     print("\n==============")


import random
min = 1
max = 10
count = 0
target = random.randint(min,max)
print("============猜數字遊戲=================\n")
while(True):
    count += 1
    try:       
        keyin = int(input(f"猜數字的範圍{min}~{max}:"))
    except:
        print('請輸入整數!')
        continue

    if(keyin >= min and keyin <= max):
        if keyin == target:
            print(f"賓果!猜對了, 答案是:{keyin}")
            break
        else:
            print("請再努力!!!!")
            continue
    else:
        print("請輸入提示範圍內的數字")
print(f"您猜了{count}次")
print("遊戲結束")


