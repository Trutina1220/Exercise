# number 1
# inventory = {
#  'gold' : 500,
#  'pouch' : ['flint', 'twine', 'gemstone'],
#  'backpack' : ['xylophone','dagger', 'bedroll','bread loaf']
# }
# inventory['pocket'] = ['seashell','strange berry', 'lint']      #adding a new key and the value on a dictionary
# inventory['backpack'] = sorted(inventory['backpack'])           #change one of the value inside one key to become sorted
# print(inventory['backpack'])
# inventory['backpack'].remove('dagger')                          #removing a specific value in a dictionary
# print(inventory['backpack'])
# inventory['gold'] = inventory['gold'] + 50                      #adding int to a int value on a dictionary
# print(inventory['gold'])

# number 2
# prices = {
#     'banana':[4,2],
#     'apple':[2,3],
#     'orange': [1.5,5],
#     'pear': [3,3]
# }
# for x,y in prices.items():                      #looping through a dictionary to get the value
#     print(x,'\nprice:',y[0],'\nstock:',y[1])
# total = 0
# for y in prices.values():                  #looping the items
#     total += (y[0] * y[1])
# print(total)

#number 3               #making simple function on dictionary
# stock = {
#  "banana": 6,
#  "apple": 0,
#  "orange": 32,
#  "pear": 15
# }
# prices = {
#  "banana": 4,
#  "apple": 2,
#  "orange": 1.5,
#  "pear": 3
# }
# def compute_bill():
#     food = input('Enter the food: ')
#     total = 0
#     if stock[food]>0:
#         total += prices[food]
#         stock[food] = stock[food]-1
#     return total,stock[food]
# print(compute_bill())

#number 4
# eren = {
#  "name": "Eren",
#  "homework": [90.0,97.0,75.0,92.0],
#  "quizzes": [88.0,40.0,94.0],
#  "tests": [75.0,90.0]
# }
# mikasa = {
# "name": "Mikasa",
# "homework": [100.0, 92.0, 98.0, 100.0],
# "quizzes": [82.0, 83.0, 91.0],
# "tests": [89.0, 97.0]
# }
# armin = {
# "name": "Armin",
# "homework": [0.0, 87.0, 75.0, 22.0],
# "quizzes": [0.0, 75.0, 78.0],
# "tests": [100.0, 100.0]
# }
# students = [eren,mikasa,armin]
# # for student in students:
# #     for x,y in student.items():
# #         print(x,y)
# def average(numbers:list):
#     total = float(sum(numbers)) / len(numbers)
#     return total
# print(average(armin['tests']))
# def get_average(students):
#     homework = float((sum(students['homework'])/len(students['homework'])))
#     quiz = float((sum(students['quizzes']) / len(students['quizzes'])))
#     tests = float((sum(students['tests']) / len(students['tests'])))
#     the_average = (homework*10/100)+(quiz*30/100)+(tests*60/100)
#     return the_average
# print(get_average(mikasa))
# def get_letter_grade(score):
#     if score >= 90:
#         return 'A'
#     elif score >=80 and score < 90:
#         return 'B'
#     elif score >= 70 and score < 80:
#         return 'C'
#     elif score >=60 and score <70:
#         return 'D'
#     else:
#         return 'F'
# print(get_letter_grade(get_average(mikasa)))
#
# def get_class_average(students):
#     results=[]
#     for i in students:
#         results.append(get_average(i))
#     the_class_average = average(results)
#     return the_class_average
# print(get_class_average(students))
# print(get_letter_grade(get_class_average(students)))

#EXTRA PRIME NUMBERS
def find_the_prime_numbers_with_index():
    number= int(input('Enter the index of the prime number: '))
    starting_number = 8
    prime_numbers=[2,3,5,7]
    while len(prime_numbers) < number:
        if number<1:
            print("there's no prime number with that index")
            exit()
        if starting_number % 2 != 0 and starting_number % (3) != 0 and starting_number % (5) != 0 and starting_number % (7) != 0:
            prime_numbers.append(starting_number)
        starting_number += 1
    return (prime_numbers[number-1])
print(find_the_prime_numbers_with_index())