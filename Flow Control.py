# number 1(find the max of 2 numbers)
# def max(x,y):
#     if x > y :
#         return x
#     else:
#         print(y)
#         return y
# max(5,10)
# max(10,10)

# number 2(find the max of 3 numbers)
# def max_of_three_numbers(x,y,z):
#     if x>y and x>z:
#         print(x)
#         return x
#     elif y>x and y>z:
#         print(y)
#         return y
#     else:
#         print(z)
#         return z
# max_of_three_numbers(4,10,12)

# number 3(count the list or string)
# def count_it(x):
#     i = 0
#     for p in x:
#         i += 1
#     print(i)
#
# list = [10,20,10,30]
# count_it(list)

# number 4 (find the vowel)
# vowel = ["a","i","u","e","o"]
# def find_vowel():
#     words = input("enter the words: ")
#     for o in words:
#         if o in words:
#             return True
#             exit()
#         else:
#             return False
#             exit()
# print(find_vowel())

# number 5 (reversing word )
# def reverse():
#     words = input("enter the words: ")
#     string_lenght =  len(words)
#     slice_string = words[string_lenght::-1]
#     print(slice_string)
#
# reverse()

# number 6 (checking palindrome)
# def find_the_palindrome():
#     words = input("enter the words: ")
#     words_lenght = len(words)
#     reverse_words = words[words_lenght::-1]
#     if words == reverse_words:
#         return True
#     else:
#         return False

# print(find_the_palindrome())

# number 7 (palindrom in a phrases)
# def phrases_palindrome():
#     phrase = input("enter the phrase: ")
#     words_in_phrases = []
#     phrase_lenght = len(phrase)
#     not_included =[" ", ".", '"', ",","?","!","'"]
#     words_clean = ""
#     for i in phrase:
#         if i not in  not_included:
#             words_clean += i
#     x = words_clean[len(words_clean)::-1]
#     if words_clean == x:
#         return True
#     else:
#         return False

# print(phrases_palindrome())

# number 8

# def generate_n_chars(int,str):
#     word = str
#     number_of_times = 0
#     for i in range(int):
#         number_of_times += 1
#         word += str
#     if number_of_times == int:
#         return(word)
#
# print(generate_n_chars(5,"x"))

# number 10
def grading():
    score = float(input("Enter the score: "))
    if score > 1.0 or score < 0:
        return ("Error")
    elif score >= 0.9:
        return ("A")
    elif score >= 0.8:
        return ("B")
    elif score >= 0.7:
        return ("C")
    elif score >= 0.6:
        return ("D")
    elif score < 0.6:
        return ("F")

print(grading())





























