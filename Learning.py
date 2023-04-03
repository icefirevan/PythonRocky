# str1 = 'QYTANG'
# str2 = 'day'
# str3 = '2014-9-28'
# print(str1 + '\'' + str2 + ' ' + str3)


# word = 'scallywag'
# sub_word = word[2:6]
# print(sub_word)

# str1 = 'Python'
# str_new = str1[1:] + '-' + str1[:1] + 'y'
# print(str_new)

department1 = 'security'
department2 = 'Python'
depart1_m = 'cq_bomb'
depart2_m = 'qinke'
COURSE_FEES_SEC = 456789.12456
COURSE_FEES_Python = 1234.3456

# 方案一：字符串格式化表达式
line1 = 'Department1 name:%-12sManager:%-12sCOURSE FEES:%-12.2fThe End!'%(department1, depart1_m, COURSE_FEES_SEC)
line2 = 'Department2 name:%-12sManager:%-12sCOURSE FEES:%-12.2fThe End!'%(department2, depart2_m, COURSE_FEES_Python)

# 方案二：字符串格式化方法
line1 = 'Department1 name:{:<12}Manager:{:<12}COURSE FEES:{:<12.2f}The End!'.format(department1, depart1_m, COURSE_FEES_SEC)
line2 = 'Department2 name:{:<12}Manager:{:<12}COURSE FEES:{:<12.2f}The End!'.format(department2, depart2_m, COURSE_FEES_Python)

# 方案三：格式化字符串f-string（自己补充练习）
line1 = f'Department1 name:{department1:<12}Manager:{depart1_m:<12}COURSE FEES:{COURSE_FEES_SEC:<12.2f}The End!'
line2 = f'Department2 name:{department1:<12}Manager:{depart2_m:<12}COURSE FEES:{COURSE_FEES_Python:<12.2f}The End!'

length = len(line1)
print('='*length)
print(line1)
print(line2)
print('='*length)
