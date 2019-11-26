# number 1
# list_1 = [1,2,3,4,5]
# print(len(list_1))
# print(lenght(list_1))         #there's no lenght() func at all

#number 2
#false
# the first number in a list started with 0 in python

#number 3
# xlist = []
# xlist.append(5)
# xlist.append(10)
# print(xlist)              #the outpot shows [5,10]

#number 4
# zlist = []
# zlist.append([3, 4])
# zlist.append(1,2,3,4)         # this will produce error , cause append only accept 1 argument only
# print(zlist)                 #the output shows [[3,4]]
# print(len(zlist))

# number 5
# xlist2 = list(range(-3,3))    #the range synthax use the argument (start,finish,step)
# print(xlist2)                 #the output should be [-3,-2,-1,0,1,2]

# number 6
# xlist3 = list(range(-3, 3, 3))
# print(xlist3)                 #the output should be [-3,0]

#number 7
# xlist4 = list(range(-3))
# print(xlist4)                   #the output should be []

#number 8
# xlist = [2, 1, 3]
# ylist = xlist.sort()
# print(xlist, ylist)       #the ouput should be [1,2,3] None

#number 9
# def multiply_list(start, stop):
#     product = 1
#     for element in range(start, stop):        #the inrange stop index doesnt include the last number
#         product = product * element
#     return product
# x = multiply_list(1, 4)         #the output is 5

# number 10
# def f1(x, y):
#     print([x, y])     #doesn't return anything , it just printing the value

#number 11
# def f2(x, y):
#     return x, y       #this function return it

#number 12
# def f3(x, y):
#     print(x, y)
#     return [x, y]     #True

# number 13
# def f4(x, y):
#     return [x, y]
#     print(x, y)         #True

# # number 14
# def f5(x, y):
#     return [x, y]
#     print([x, y])         #True

# number 15
# xlist = [3, 2, 1, 0]
# for item in xlist:
#     print(item,end="")    #produce 3210

# number 16
# a = 1
# b = 2
# xlist = [a, b, a + b]
# a = 0                 #when you change the value of variable in the list , the list doesnt change
                        #the list used the value before the list was declared
# b = 0
#                       #output are [1, 2 3]
# print(xlist)


#number 17
# xlist = [3, 5, 7]             #produce error
# print(xlist[1] + xlist[3])    #index[3] is out of range / not declared yet

# #number 18
# xlist = ["aa", "bb", "cc"]
# for i in [2, 1, 0]:
#     print(xlist[i], end=" ")  #produce cc bb aa

#number 19
# for i in range(1,10,2):
#     print(i)              #print odd number (1 until 9)

#number 20
# x =list(range(5))     #by defaul start at 0 ends at 5

#number 21
# for i in range(4):
#     print(i)

# number 22
# def main():
#     num = eval(input("Enter a number: "))
#     for i in range(3):
#         num = num * 2
#     print(num)                #output 16
# main()

#number 23
# fact = 1
# for factor in range(4):
#     fact = fact * factor          #produce 0
# print(fact)

#number 24
# def main():
#     n = eval(input("Enter an integer: "))
#     ans = 0
#     for x in range(1, n):
#         ans = ans + x
#     print(ans)        #produce 10
# main()

#number 25
# s =['s','c','o','r','e']
# for i in range(len(s) - 1, -1, -1):
#     print(s[i], end = " ")            #produce e,r,i,c,s

#number 26
# s =['s','c','o','r','e']
# sum = 0
# for i in range(len(s)):
#     sum = i + s[i]        #basically this is  int + string
# print(sum)                # gonna produce error

#number 27
# s =['s','c','o','r','e']
# sum = 0
# for i in range(len(s)):
#     sum =  s[i] + i        #basically this is  string + int
# print(sum)                # gonna produce error

#number 28
# def summer1(n):
#     sum = 0
#     for i in range(1, n + 1):
#         sum = sum + i
#     return sum
# print(summer1(3))     #return 6

#number 29
# def summer2(n):
#     sum = 0
#     for i in range(n):
#         sum = sum + i
#     return sum            #produce 6
# print(summer2(4))

#number 30
# def foo():
#     xlist = []
#     for i in range(4):
#         x = input("Enter a number: ")
#         xlist.append(x)
#     return xlist                  #this function makes user input something , and make it into list
# print(foo())














