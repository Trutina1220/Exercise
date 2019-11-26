 # number 1 (taking date and make it to list and tuple)
# def make_it():
#     numbers= (input('enter numbers: '))
#     the_list = []
#     the_tuple = (numbers)
#     for i in numbers [0::2]:
#         the_list.append(i)
#     print('List: ',the_list)
#     print('Tuple: '+'('+the_tuple+')')
# make_it()
#
# number 2 (translate text )
# def translate(text):
#     text:str = text
#     vocals = ['a','i','u','e','o']
#     translated_text: str = ''
#     for i in text:
#         if i in vocals:
#             translated_text += i
#         else:
#             translated_text += i+'o'+i
#
#     return translated_text
#
# print(translate('power'))

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

# number 5
# def overlapping(list_1, list_2):
#     for i in list_1:
#         for j in list_2:
#             if i == j:
#                 return True
#     return False
# print(overlapping((2, 4, 6), (1, 5, 7)))


# number 6 (make histogram)
def histogram(list_1):
    for i in list_1:
        histogram = i*'*'
        print(histogram)
histogram((4,9,7))
