import random

def playGame():
    min = 1
    max = 100
    count = 0
    target = random.randint(min,max)
    print(target)
    print("============猜數字遊戲=================\n")
    while(True):
        keyin = int(input(f"猜數字的範圍{min}~{max}:"))
        count += 1
        if(keyin >= min and keyin <= max):
            if keyin == target:
                print(f"賓果!猜對了, 答案是:{keyin}")
                break
            elif keyin > target:
                print("再小一點")
                max = keyin - 1
            elif keyin < target:
                print("再大一點")
                min = keyin + 1
            print(f"加油@您已經猜了{count}次")
            continue
        else:
            print("請輸入提示範圍內的數字")
    print(f"您猜了{count}次")

class student():
    def __init__(self,na:str,ma:int,en:int,ch:int):
        self.name = na
        self.math = ma
        self.english = en
        self.chinese = ch   

    def sum(self) -> int:
        return self.math + self.english + self.chinese
    
def getStudent(name:str,chinese:int,math:int,english:int) -> student:
    return student(na=name,ch=chinese,en=english,ma=math)


