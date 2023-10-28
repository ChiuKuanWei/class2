import pyinputplus as pyip
#註解全段快捷鍵:Ctrl+/

# ------------------------------------------------------------------------
# name = '邱冠為'
# source = pyip.inputInt("請輸入學生分數(最高300分):",min=0,max=300)
# print(f"\n學生:{name}的分數為{source}")
# isYes = pyip.inputMenu(['Y', 'N'], prompt="學生是否符合加分條件?", numbered=True,lettered=False) #numbered= 1.Y 2.N #lettered= A.Y B.N 
# if isYes == 'Y':
#     print('符合')
# else:
#     print('不符合')
# ------------------------------------------------------------------------


#巢狀選擇
#• 如果x不是負數，則傳回值為 x ** (1 / y)。
#• 如果x是負數而且為偶數，則傳回值為"虛數"。
#• 如果x是負數而且為奇數，則傳回值為 -(-x) ** (1 / y)
# ------------------------------------------------------------------------
# x = pyip.inputInt("請輸入隨機整數(限制-10~10):",min=-10,max=10)
# y = pyip.inputInt("請輸入隨機整數(限制-10~10):",min=-10,max=10)
# if x >= 0:
#     x = x ** (1/y)
#     print(f'正數結果:{x}')
# else:
#     if x%2 == 0:
#         print(f'負數結果:虛數')
#     else:
#         x = -(-x) ** (1/y)
#         print(f'負數結果:{x}')
# ------------------------------------------------------------------------

# ------------------------------------------------------------------------
get_total = 0
input_price = pyip.inputInt("請輸入購買金額:")

if input_price >= 100000: #打8折
    get_total = input_price * 0.8
elif input_price >= 50000 and input_price < 100000: #打85折
    get_total = input_price * 0.85
elif input_price >= 30000 and input_price < 50000: #打9折
    get_total = input_price * 0.9
elif input_price >= 10000 and input_price < 30000: #打95折
    get_total = input_price * 0.95
else:
    get_total = input_price
print(f'實付金額是:{get_total}元')
# ------------------------------------------------------------------------
