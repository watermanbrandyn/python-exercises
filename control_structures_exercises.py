#1. A. Prompt user for a day of the week, print whether Monday or not.
user_day = input("Please provide a day of the week: ")
user_day = user_day.lower()
if user_day == 'monday':
    print('You chose Monday!')
else:
    print('You did not choose Monday.')

#1. B. Prompt user for a day of the week, print whether weekday or weekend. 
user_week = input("Please provide a day of the week (again): ")
user_week = user_week.lower()
weekdays = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday']
weekends = ['saturday', 'sunday']
if user_week in weekdays:
    print("That choice is a weekday!")
elif user_week in weekends:
    print("That choice is a weekend!")
else:
    print("That is not a valid choice.")

#1. C. Create variables and assign values for: number of hours worked in one
#week, the hourly rate, how much the week's paycheck will be (1 1/2 * for OT)
hours_worked = 45.00
hourly_rate = 25.00
overtime = False
if hours_worked > 40:
    overtime = True
paycheck = 0.00
if overtime == False:
    paycheck = hours_worked * hourly_rate
elif overtime == True:
    ot_hours = hours_worked - 40
    paycheck = (40 * hourly_rate) + ((1.5 * hourly_rate) * ot_hours)
print(f"Total pay this week is: ${paycheck}!")

#2. A. While Loops:
i = 5
while i <= 15:
    print(i)
    i += 1
num = 0
while num < 100:
    print(f"{num}\n")
    num += 2
    if num == 100:
        print(num)
#num = 100
while num > -10:
    print(num)
    num -= 5
    if num == -10:
        print(num)

num = 2
while num < 1000000:
    print(num)
    num = num**2

num = 100
while num > 5:
    print(num)
    num -= 5
    if num == 5:
        print(num)

#2. B. For loops:
user_num = input("Please provide a number: ")
user_num = int(user_num)
for x in range(1,11):
    output = x * user_num
    print(f"{user_num} x {x} = {output}")

for x in range(1,10):
    x2 = str(x)
    print(f"{x2 * x}")

#2. C. break and continue
while True:
    user_odd = input("Please give an odd # between 1 and 50 to exclude: ")
    if user_odd.isdigit() == True and int(user_odd) < 50 and (int(user_odd) % 2 == 1):
        break
user_odd = int(user_odd)
print(f"Number to skip is: {user_odd}\n")
x = 1
while x < 50:
    if x != user_odd:
        print(f"Here is an odd number: {x}")
        x += 2
        continue
    elif x == user_odd:
        print(f"Yikes! Skipping number: {user_odd}")
        x += 2
# for x in range(1, 51):
#     if x % 2 == 1 and x != user_odd:
#         print(f"Here is an odd number: {x}")
#     elif x == user_odd:
#         print(f"Yikes! Skipping number: {user_odd}")

#2. D. counting to input
valid = False
while valid != True:
    user_num = input("Please enter a positive whole number: ")
    if user_num.isdigit() == True and int(user_num) > 0 and isinstance(int(user_num), int) == True:
        valid = True
user_num = int(user_num)
for x in range(0, (user_num +1)):
    print(x)

#2. E. counting down from input to 1
valid = False
while valid != True:
    user_num = input("Please enter a positive whole number: ")
    if user_num.isdigit() == True and int(user_num) > 0 and isinstance(int(user_num), int) == True:
        valid = True
user_num = int(user_num)
while user_num > 0:
    print(user_num)
    user_num -= 1

#3. fizzbuzz
for x in range(1, 101):
    if x % 3 == 0 and x % 5 == 0:
        print("Fizzbuzz")
    elif x % 5 == 0:
        print("Buzz")
    elif x %3 == 0: 
        print("Fizz")
    else:
        print(x)

#4. Display a table of powers
cont = True
while cont == True: 
    user_num = input("What number would you like to go up to? ")
    user_num = int(user_num)
    numbers = []
    squares = []
    cubes = []
    for i in range(1, (user_num + 1)):
        numbers.append(i)
        squares.append(i**2)
        cubes.append(i**3)
    table = zip(numbers, squares, cubes)
    print("\nHere is your table!\n")
    print("{:<8} {:<8} {:<8}".format('number', 'squared', 'cubed'))
    for i in table:
        number, squared, cubed = i
        print("{:<8} {:<8} {:<8}".format(number, squared, cubed))
    user_cont = input("Would you like to go again?(Y/N) ")
    if user_cont == 'N':
        cont = False
#Escaping the while loop is very limited to 'N'.

#5. Convert grades into letter grades.
keep_grading = True
while keep_grading:
    num_grade = input("Please enter a number grade: ")
    num_grade = int(num_grade)
    if num_grade < 60:
        print("That is an F.")
    elif num_grade < 67 and num_grade > 59:
        print("That is a D.")
    elif num_grade < 80 and num_grade > 66:
        print("That is a C.")
    elif num_grade < 88 and num_grade > 79:
        print("That is a B.")
    else:
        print("That is an A.")
    keep_going = input("Would you like to keep grading?(Y/N) ")
    if keep_going == 'N': 
        keep_grading = False
#Same as above, escaping is very limited to 'N'.

#6. List of dictionaries
books = [
{
'title': 'Tuesdays with Morrie', 
'author': 'Mitch Albom', 
'genre': ['Biography', 'Memoir']
},
{
'title': 'The Art of War', 
'author': 'Sun Tzu', 
'genre': ['Strategy', 'Philosophy']
}, 
{
'title': 'The Giver',
'author': 'Lois Lowry',
'genre': 'Science Fiction'
},
{
'title': 'Notes of a Native Son',
'author': 'James Baldwin',
'genre': ['Essay', 'Non-Fiction']
}
]
for index in range(len(books)):
    for key in books[index]:
        print(f"{key}: {books[index][key]}")
#Will print all the information, but does not separate the genres. Leaves []
#6. A. Print titles given a genre.
user_pref = input("Please enter a genre: \n")
for index in range(len(books)):
    for key in books[index]:
        if user_pref in books[index][key]:
            print(books[index]['title'])






        

















