import numpy as np
#============================list=======================================
# #             0        1        2       3       4        5        6
# weekdays = ["星期一","星期二","星期三","星期四","星期五","星期六","星期七"]
# #            -7       -6       -5       -4      -3      -2       -1

# #取前三名
# lead_three = weekdays[:3]
# print(lead_three)

# #後三名
# last_three = weekdays[-3:]
# print(last_three)


# for day in weekdays:
#     print(f'week:{day}')

thriller = ['Thriller', 'Billie Jean', 'Beat It']
thriller.append('That Girl is Mine')
print(thriller)
thriller.insert(1,"John Weak")
print(f'插入了{thriller[1]}:{thriller}')

bad = ['Bad','Smooth Criminal','Speed Demon','Man in the Mirror','Dirty Diana']
print(bad)
popped = bad.pop()
print(f'{popped}被刪除了')


#把 bad_2 這個 list 加到 bad_1 中整合，要把第二個 list 中的元素 (而不是整個 list) 加到第一個 list 中的做法，就是改成使用 extend
bad_1 = ['Bad1', 'Smooth Criminal1','Speed Demon1']
bad_2 = ['Man in the Mirror2', 'Dirty Diana2']
bad_1.extend(bad_2)
print(f'bad_2已新增至bad_1:{bad_1}')

students = []
stud1 = [10,20,30,40]
stud2 = [50,60,70,80]
stud3 = [90,100,110,120]
students.append(stud1)
students.append(stud2)
students.append(stud3)
arr = np.array(students)
print(arr)
print(arr.shape)

#=======================================================================

#============================dictionary=================================
             
cars_price = {"volvo":"240萬" , "toyota":"100萬" , "Ford":"80萬"}

# #取前三名
# lead_three = weekdays[:3]
# print(lead_three)

# #後三名
# last_three = weekdays[-3:]
# print(last_three)


# for day in weekdays:
#     print(f'week:{day}')

#=======================================================================