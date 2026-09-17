#定义
# t1 = (11,22,33,44)
# print(type(t1))
#
# print(t1[2])
#
# #count  统计个数
# #index  找到第一个位置
# print(t1.index(44))
# print(t1.count(44))
#
#
# t1 = (1,3,4,4,555,55,33)
# # a,b,c,d,e,f,g = t1
# # print(a,b,c,d,e,f,g)
#
# *z,v = t1
# print(*z)



students = (
("s001", "王林", 85, 92, 78),
("s002", "李慕婉", 92, 88, 95),
("S003", "十三", 78, 85, 82),
("S004", "曾牛", 88, 79, 91),
("S005", "周轶", 95, 96, 89),
("S006", "王卓", 76, 82, 77),
("S007", "红蝶", 89, 91, 94),
("S008", "徐立国", 75, 69, 82),
("S009", "许木", 86, 89, 98),
("S010", "通天", 66, 59, 72),
)

#1.计算每个学生总分,各科平均分,然后一并输出出来
#方式一
# print("学号\t\t姓名\t\t语文\t\t数学\t\t英语\t\t总分\t\t平均分")
# for s in students:
#     total = s[2]+s[3]+s[4]
#     avg = total / 3
#     print(f"{s[0]} \t {s[1]} \t {s[2]} \t {s[3]} \t {s[4]} \t {total} \t {avg : .1f}")
#方式二
print("学号\t\t姓名\t\t语文\t\t数学\t\t英语\t\t总分\t\t平均分")
for id,name,c,m,e in students:
    total = c+ m + e
    avg = total / 3
    print(f"{id} \t {name} \t {c} \t {m} \t {e} \t {total} \t {avg : .1f}")


#2,统计各科成绩最高分,最低分,平均分,并输出
#2.1 获取成绩
chinese_scores = [s[2] for s in students ]
match_scores = [s[3] for s in students ]
english_scores = [s[4] for s in students ]
#2.2 找到并输出
print(f"语文最低分 {min(chinese_scores)}, 语文最高分 {max(chinese_scores)} ,语文平均分 {sum(chinese_scores)/len(chinese_scores)}")
print(f"数学最低分 {min(match_scores)}, 数学最高分 {max(match_scores)} ,数学平均分 {sum(match_scores)/len(match_scores)}")
print(f"英语最低分 {min(english_scores)}, 英语最高分 {max(english_scores)} ,英语平均分 {sum(english_scores)/len(english_scores)}")

#3,查找),并输出
# print("优秀学生(成绩大于90")
# for s in students:
#     total = s[2]+s[3]+s[4]
#     avg = total / 3
#     if avg >= 90:
#         print(f"学号{s[0]} ,姓名{s[1]} ,平均分{avg: .1f}")
print("优秀学生(成绩大于90")
for id,name,c,m,e  in students:
    total = c+ m + e
    avg = total / 3
    if avg >= 90:
        print(f"学号{id} ,姓名{name} ,平均分{avg: .1f}")










