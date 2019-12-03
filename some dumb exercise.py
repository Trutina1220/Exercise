#FIND THE PRIME NUMBERS
_range= int(input('Enter the range of numbers: '))
number= int(input('Enter the index of the prime number: '))
prime_numbers=[2,3,5,7]
for i in range (8,_range):
    if i%2 != 0 and i%(3) != 0 and i%(5) != 0 and i%(7) != 0:
        prime_numbers.append(i)
print(prime_numbers[number-1])



