#
# max = int(input("please input a mun to do factorial："))
# while max < 1 or max > 100:
#     print("please input mun between 1- 100")
#     max = int(input("please input a mun to do factorial："))
# sum = 1
# while max > 0:
#     sum *= max
#     max = max - 15
#     if sum % 5 == 0:
#         print("sum = ", sum)
# print("total sum = ", sum)

count = 0
i = 1
while i <= 100:
    if (i % 3 == 0 or i % 7 == 0) and (i % 21 != 0) :
        count += 1
    i += 1
print(count)
