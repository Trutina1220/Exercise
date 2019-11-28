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

#number 7
# def find_the_number_word(a=[]):
#     list_of_len_words = []
#     for i in a:
#         list_of_len_words.append(len(i))
#     print(list_of_len_words)
# find_the_number_word(a=['gogo','lamakunta','terbang'])

# number 8(find the longest word in a list )
# def find_longest_word(a=[]):
#     list_of_len_words = []
#     for i in a:
#         list_of_len_words.append(len(i))
#     print(max(list_of_len_words))
# find_longest_word(a=['jackass','lokenghong','losapaanjing'])

# number 9
# def filter_long_words(a:int,words:list =[]):
#     the_big_words=[]
#     for i in words:
#         if len(i) > a:
#             the_big_words.append(i)
#     return (the_big_words)
# print(filter_long_words(3,['apa','kuda','makanan']))

#number 10
# def find_pangram():
#     alphabet:list=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',' ']
#     the_checked_words=[]
#     sentence:str = input('enter the sentence: ')
#     sentence = sentence.lower()
#     for i in alphabet:
#         if i in sentence:
#             the_checked_words.append(i)
#     if the_checked_words == alphabet:
#         return True
#     else:
#         return False
# print(find_pangram())

#number 11
# def char_freq(a:str):
#     this_dict={}
#     for i in a:
#         if i not in this_dict:
#             this_dict[i] = 0
#         if i in this_dict:
#             this_dict[i] += 1
#     print(this_dict)
#
# char_freq('memekke')


# number 12
# def translate_caesar_cipher(a:str):
#     alphabet:list=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
#     the_translate =''
#     for i in a:
#         x = alphabet.index(i) + 13
#         if x > 25:
#             x = x-26
#         the_translate += alphabet[x]
#     print(the_translate)
# translate_caesar_cipher('o')

#number 13
# def makeForms():
#     verb_:str = input('enter the infinitive verb: ')
#     verb_1:str = verb_
#     if verb_.endswith("y"):
#         verb_1 = verb_.rstrip('y')  + 'ies'
#     elif verb_.endswith('o') or verb_.endswith('ch') or verb_.endswith('s') or verb_.endswith('sh') or verb_.endswith('x') or verb_.endswith('z'):
#         verb_1 = verb_ + 'es'
#     else:
#         verb_1 = verb_ + 's'
#     return verb_1
# print(makeForms())

# # # number 14
# def make_forming():
#     vocals = ['a','i','u','e','o']
#     verb_:str = input('enter the infinitive verb: ')
#     verb_ing: str = verb_
#     for letter in verb_:
#         if verb_[-2] in vocals and verb_[-1] not in vocals and verb_[-3] not in vocals:
#             verb_ing = verb_+verb_[-1]+'ing'
#             return verb_ing
#     if verb_.endswith('e') and verb_.endswith('ee'):
#         verb_ing = verb_ + 'ing'
#         return verb_ing
#     elif verb_.endswith('ie'):
#         verb_ing = verb_.rstrip('ie')+'ying'
#         return verb_ing
#     elif verb_.endswith('e'):
#         verb_ing= verb_ing.rstrip('e') +'ing'
#         return verb_ing
#     else:
#         verb_ing = verb_ing +'ing'
#         return verb_ing
# print(make_forming())
