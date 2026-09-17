#集合set  定义  无序,不可重复,可修改
# s1 = {13,14,65,78,34,12,3,4,5,6,7,2,2,3,4,5,6,7,2}
# print(s1)
# print(type(s1))
#
# s2 = set()
# print(s2)
# print(type(s2))

# 选修足球学生名单
football_set = {"王林", "曾牛", "徐立国", "遁天", "天运子", "韩立", "厉飞雨", "乌丑", "紫灵"}
# 选修篮球学生名单
basketball_set = {"张铁", "墨居仁","王林", "姜老道", "曾牛", "王蝉", "韩立", "天运子", "李化元", "厉飞雨", "云露"}
# 选修法语学生名单
french_set = {"许木", "王卓", "十三", "虎咆", "姜老道", "天运子",  "红蝶", "厉飞雨", "韩立", "曾牛"}
# 选修艺术学生名单
art_set = { "遁天", "天运子", "韩立", "虎咆", "姜老道", "紫灵"}

#1.找出同时选修法语和艺术的  &(交集)
# fa_sat = french_set.intersection(art_set)
fa_sat = french_set  & art_set
print(fa_sat)

#2.四个都选了
# sat = football_set.intersection(basketball_set.intersection(french_set.intersection(art_set)))
all_set = football_set & basketball_set & french_set & art_set
print(all_set)

#3.只选了足球,没选篮球  -(差集)
# fb_set = football_set.difference(basketball_set)
fb_set = football_set  -  basketball_set
fb_set1 = { s for s in football_set  if s not in basketball_set}
print(fb_set)
print(fb_set1)

#4.统计每个选修的课程数量
#4.1 获取学生名单   并集(|)

all_set = football_set | basketball_set | french_set | art_set
print(all_set)

#4.1 获取重复元素
all_list = [*football_set, *basketball_set, *french_set, *art_set]
print(all_list)

for s in all_set:
    print(f"{s} 选修了 {all_list.count(s)} 课程")


# 调用   import 模块名,模块名
# 给模块名起别名 import 模块名  as 别名
#  用模块名中的功能名 form 模块名 import 功能名
# 给调用模块名中的功能名起别名 form 模块名 import 功能名 as 别名
#  调用模块中所 有的功能  form 模块名 import *




