# Taking the input number

Input_num = int(input('Enter a number: '))

# Creating a list of divisors 
Divisors = []

for i in range(1,Input_num):
    if Input_num%i == 0:
        Divisors.append(i)


# Checking if the input number is  a perfect number or not.
if sum(Divisors) == Input_num:
    print('The number is a perfect number.')
else:
    print('This number is not perfect. ')

