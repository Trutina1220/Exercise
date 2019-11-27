 # number 1 (taking date and make it to list and tuple)
# def make_it():
#     numbers= "3,5,7,23"
#     numbers= numbers.replace(',',' ')
#     print(numbers)
#     newlist= numbers.split()                  #Introducing the in built function of replace and split
#     print(newlist)                            if you declare the new type of variable , it will change the date type
#     print('list: ', str(newlist))             split = takes a string and make it into a list
#     print('tuple:', tuple(newlist))
# make_it()


#ver 2.0
# numbers = "3,5,7,23"
# numbers = numbers.replace(',',' ')
# newlist = numbers.split()
# print('list:', str(newlist))
# print('tuple', str(tuple(newlist)))
#
# number 2 (translate text )
# def translate(text):
#     text:str = text
#     vocals = ['a','i','u','e','o',' ']
#     translated_text: str = ''                 #added space in the vocals
#     for i in text:
#         if i in vocals:
#             translated_text += i
#         else:
#             translated_text += i+'o'+i
#
#     return translated_text
#
# print(translate('this is fun'))

# # number 3 (make calendar)
# import calendar
# c = calendar.TextCalendar(calendar.MONDAY)
# str = c.formatmonth(2019,5)
# print(str)

# number 4
# def _member(val):
#     a = ['baju', 9 , 'nomor','kuda' , 2.1]
#     if val in a:
#         return True
#     else:
#         return False
# print(_member('mantap'))
# print(_member(9))

#ver 2.0

# arr = ['a','b','c']
# def is_member(x,a=[]):
#     for i in a:
#         if(i==x):                             #argument ... just treat it as declaring a variable
#             return True
#     return False
# print(is_member(3,arr))
# print(is_member('d',arr))

# number 5
# def overlapping(list_1, list_2):
#     for i in list_1:
#         for j in list_2:
#             if i == j:
#                 return True
#     return False
# print(overlapping((2, 4, 6), (1, 5, 7)))


# number 6 (make histogram)
# def histogram(a=[]):
#     for i in a:
#         histogram = i*'*'             #tweaking the argument 
#         print(histogram)
# histogram(a=[4,9,7])
