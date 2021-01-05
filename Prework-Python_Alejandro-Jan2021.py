#Alejandro Beltran python 5 questions prework

#Question 1
def hello_name(user_name):
    return "hello_" + user_name.upper() + "!"

#Question 2 if ods in firs 100 numbers
x = range(0, 100)
for n in x:
    if n % 2 != 0:
        print(n)

#Question 2 if first 100 odd numbers
numbers = range(0, 1000)
odd_100 = []
for odd in numbers:
    if len(odd_100) > 99:
        break
    elif odd % 2 != 0:
        odd_100.append(odd)
print(odd_100)
print(len(odd_100))

#Question 3
ages = [48, 67, 26, 13, 57, 63, 42, 9, 33, 43, 23]
def max_num_in_list(a_list):
    print(max(a_list))
max_num_in_list(ages)

#Question 3
ages = [48, 67, 26, 13, 57, 63, 42, 9, 33, 43, 23]
def max_num_in_list(a_list):
    high = float('-inf')
    for n in a_list:
        if n > high:
            n == high
    print(n)
max_num_in_list(ages)

#Question 4
def is_leap_year(a_year):
    if a_year % 4 == 0 and a_year % 100 != 0:
        print('true')
    elif a_year % 4 == 0 and a_year % 400 == 0:
        print('true')
    else:
        print('false')
is_leap_year(2024)

#Question 5
con = [2,3,4,5,6,7]
uncon = [1,2,4,5,7,10]
def is_consecutive(a_list):
    n = 0
    x = True
    while n < len(a_list) - 1:
        if a_list[n] + 1 == a_list[n + 1]:
            n += 1
        else:
            x = False
            break
    return(x)
is_consecutive([1,2,4,5,7,10])
