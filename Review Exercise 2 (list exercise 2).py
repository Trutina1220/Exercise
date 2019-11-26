#number 1
# xlist = [1, [1, 2], [1, 2, 3]]
# print(xlist[1])           #this print index 1

#number 2
# xlist = [1, [1, 2], [1, 2, 3]]
# print(xlist[1][1])            #this print list with index 1 , in that same index , print index 2 of that item

#number 3
# xlist = [1, [1, 2], [1, 2, 3]]
# print(xlist[1] + [1])     #print x list index 1 + [1]

# number 4
# def sum_part(xlist, n):
#     sum = 0
#     for x in xlist[n]:
#         sum = sum + x
#     return sum
# ylist = [[1, 2], [3, 4], [5, 6], [7, 8]]
# x = sum_part(ylist, 2)            #produce 11
# print(x)prod

#number 5
# (a) sum = 0
# for item in xlist:
# sum = sum + item[1]

# number 6
# for i in range(3):
# #     for j in range(3):      # produce 000012024
# #         print(i * j, end="")

# number 7
# s = "abc"
# for i in range(1, len(s) + 1):
#     sub = ""
#     for j in range(i):
#         sub = s[j] + sub
#     print(sub)        #similar to reversing letter

#number 8
# s = "grasshopper"
# for i in range(1, len(s), 2):
#     print(s[i], end="")   # output is rshpe

# #number 9
# x = [7]
# y = x
# x[0] = x[0] + 3
# y[0] = y[0] - 5       #produce 5 cause x = y = 5
# print(x, y)

#number 10
# x = [7]
# y = x
# x = [8]
# print(x, y)       #remember to execute from top

#NUMBER 11
# x = [1, 2, 3, 4]
# y = x
# y[2] = 0
# z = x[1 : ]
# x[1] = 9
# print(x, y, z)    #[1, 9, 0, 4] [1, 9, 0, 4] [2, 0, 4]

#number 12
# s = "row"
# for i in range(len(s)):
#     print(s[ : i])        #r # ro

# #number 13
# s = "stab"
# for i in range(len(s)):        #t #at #bat
#     print(s[i : 0 : -1])

#number 14
# s = "stab"
# for i in range(len(s)):
#     print(s[i : -5 : -1])
                                    # s
                                    # ts  output
                                    # ats
                                    # bats

#number 15
# s = "stab"
# for i in range(len(s)):
#     print(s[0 : i : 1])
                                    #output are
                                    # s
                                    # st
                                    # sta


