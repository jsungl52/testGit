#create a list
#variable name = [element1, element2, element3...]

# name = ['zhangsan', 'lisi', 'wangwu', 'zhaolkiu', 'jiaqi', 'lisi']
# count = 0
# revcount = len(name)
# for i in name:
#     if i == 'lisi':
#         tem = revcount * -1 + count
#         print(i, count, tem)
#     count += 1

list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
count = 1
for i in list:
    if i % 2 == 0:
        print("第{}个偶数{}".format(count, i))
        count += 1