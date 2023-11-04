import day4_tools
from day4_tools import getStudent

    
def main(BooL:bool=True):   
    while(True):   
        if BooL == True:    
            day4_tools.playGame()
        playAgain = input("您還要繼續嗎(y,n)?")
        if playAgain.lower() == 'n':
            BooL = False
            break
        elif playAgain.lower() == 'y':
            BooL = True
            continue
        else:
            print('請輸入\'y\' or \'n\'')
            BooL = False
        
    print("遊戲結束")

if __name__ == "__main__":
    main()



stud1 = getStudent('David', 80, 70, 60)
print(stud1.name)
print(stud1.math)
print(stud1.english)
print(stud1.chinese)
print(stud1.sum())