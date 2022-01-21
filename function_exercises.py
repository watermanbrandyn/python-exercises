#1. is_two, one input and returns T/F if str or # 2
# is_two takes one input, either a str or number, and returns a boolean based on if it is == 2
def is_two(x):
    if type(x) == int or type(x) == float:
    # determining if the input is numeric value
        if x == 2:
            return True
    # testing against condition x == 2 and returning a Boolean based on condition
        else:
            return False
    if type(x) == str:
    # determining if the input is str value
        if x.isdigit() == True and x == '2' or x == '2.0':
            return True
    # testing against condition x == '2' or x == '2.0' and returning a Boolean based on condition
        else:
            return False
is_two(-2)
is_two(2)
# Testing function using some numeric values
is_two("2")
is_two("2.0")
# Testing function using some str values
is_two("5")
# Input is first tested against conditional of type int or float, and then against conditional of value of 2 if so. 
# If it does not meet the first conditional it will be tested against type of str, and then against value of 2 using isdigit()

#2. is_vowel, True if passed str is a vowel
# is_vowel takes a single string input and returns a Boolean based on if the input is a vowel
def is_vowel(v):
    # creating a string with all the vowels, upper and lowercase, to test for condition
    vowels = 'aeiouAEIOU'
    # if statement to test if the input, v, is contained in the vowels string. Returns a Boolean value
    if v in vowels:
        return True
    else:
        return False
# Testing with vowel and consonant
is_vowel("x")
is_vowel('a')
is_vowel('aaa')
#Added lower to account for more str types and now it does not error check for non-str. Will return false for strings longer 
#a single char.
#Input is pitted against conditional of being contained within 'vowels' string.
#Does not account for the 'sometimes y' cases.

#3. is_consonant
# is_consonant, using is_vowel. Has one input, a (single char) string, and returns a Boolean value.
def is_consonant(c):
    # placing the 'c' input variable in to an if statement using the is_vowel() function. Return from is_vowel is then used
    # to determine a new Boolean that is the negation of that value. 
    if is_vowel(c) == False:
        return True
    else: 
        return False
# Testing with both a vowel and a consonant, has the same limitations as the is_vowel() function.
is_consonant('a')
is_consonant('b') 
# 
#4. Accepts string as a word. Capitalizes first letter of word if it is consonant.
# consonant_cap function, with a single input (string), weill return with first letter Capitalized if it is a consonant
def consonant_cap(str1):
    # If the first letter at index 0 is determined to be a consonant using the is_consonant() function
    # will return True, and then be tested against conditional of being == to True
    if is_consonant(str1[0]) == True:
        # if conditional is met will then return the str1 input after using the capitalize() function
        return str1.capitalize()
    # if the condition for being a consonant is not met will just return the same input string
    else:
        return
# Testing against a string that starts with a vowel, a consonant, and a digit.
cap_name = consonant_cap('andy')
print(cap_name)
cap_name = consonant_cap('brandy')
print(cap_name)
cap_name = consonant_cap('2ndy')
print(cap_name)

#5. calculate_tip, floats (tip, bill) inputs, output total
# calculate_tip function has two inputs, a numeric tip and bill, returns a single numeric output
def calculate_tip(tip, bill):
    # Testing for the input types as a bit of error checking from user. Testing for int or float values for inputs
    if (type(tip) == int or type(tip) == float) and (type(bill) == int or type(bill) == float):
    # Tip_amount is determined by multiplying the desired tip % and the bill
        tip_amount = tip * bill
    # return the tip_amount that is calculated
        return tip_amount
    # If the inputs do not meet numeric condition a statement is returned to provide different inputs to user.
    else:
        return "Please enter valid inputs."
# Testing of function with numeric inputs and one that does not contain a numeric input for both inputs. 
calculate_tip(.5, 100)
calculate_tip('25', 25)

#6. apply_discount, input original price and a discount %, return price after discount
# apply_discount has two inputs, and has a single return of a new numeric output
def apply_discount(price, discount):
    # Same as previous error checking to ensure that the inputs are numeric, testing for type int or float
    if (type(price) == int or type(price) == float) and (type(discount) == int or type(discount) == float):
    # Discount price (new_price) is determined by subtracting the discount (price * %) from the original price
        new_price = price - (price * discount)
    # returns the single output that is the new_price
        return new_price
    # if the condition for error checking is not met just returns message 'Please enter valid inputs.'
    else:
        return 'Please enter valid inputs.'
# Tested with numeric inputs and non-numeric
apply_discount(100, .2) 
apply_discount('100', .2)
#Assumes same % as above ( 0 - 1) and does not error check on inputs.

#7. handle_commas, accept string that is number w/ commas and return number
# def handle_commas(num_string):
#     return int(num_string.strip(','))
#  handle_commas(',,,,23,,,')  
 #Could be made more robust for float inputs and error checking.

# handle_commas has a single string input and a single numeric output that removes commas
def handle_commas(num_string):
    # creates a new variable and copies the contents of input to it
    new_string = num_string
    # for loop that cycles through the input variable
    for c in num_string:
        # if the condition of the index, c, is that it is a ',' 
        if c == ',':
            # then the local newly created variable will replace the ',' with '' 
            new_string = new_string.replace(c, "")
    # returns the local variable, the copy that now has commas removed, as a numeric value
    return float(new_string)
# Tested against different string inputs with the commas in varying places
handle_commas(",,,2333,,,")
handle_commas("2,,3,,")

#8. get_letter_grade, accept number and return letter grade associated w/ number
# get_letter_grade has a single input, a numeric value, and a single output, a string value
def get_letter_grade(grade):
    # multiple if conditions to test what bracket of the 'grade' the numeric value falls into
    if grade < 60:
    # grade is then reassigned the string letter grade based on numeric grade and returned as a string
        grade = 'F'
        return grade
    elif grade < 70: 
        grade = 'D' 
        return grade
    elif grade < 80:
        grade = 'C'
        return grade
    elif grade < 90:
        grade = 'B'
        return grade
    elif grade >= 90:
        grade = 'A'
        return grade
# Tested against numeric and non-numeric input. Non-numeric provides an error (is not error checked to re-prompt user)
get_letter_grade(67)
get_letter_grade('failed')
#Not error checked for invalid inputs.

#9. remove_vowels, accept string and removes vowels
# remove_vowels has a single string input and returns a string without the vowels
def remove_vowels(string1):
    # Creation of a string that contains the lower and uppercase vowels
    vowels = 'aeiouAEIOU'
    # use of a join statement attached to a for loop
    # cycles through every index in the input string and checks if they are contianed in the vowels string
    # if they are contianed they are not included in the return, and the joining '' eliminates the space left from vowels
    return ''.join([ch for ch in string1 if ch not in vowels])
# Tested against strings with vowels in different places to ensure they are all removed
remove_vowels('sausage')
remove_vowels('andy')

#10. normalize_name, accept string and return valid identifier that is: 
# anything not a valid identifier removed, leading and trailing whitespace removed,
# everything lowercase, spaces replaced with underscores
# normalize_name has a single string input and a single string output
def normalize_name(norm_this):
    # removal of whiteplace before or after characters and assigned to a new local variable
    new_that = norm_this.strip()
    # local variable is made lowercase
    new_that = new_that.lower()
    # replacement of spaces with underscores
    new_that = new_that.replace(" ", "_")
    # for loop that iterates through every index of local variable to check against special characters
    # join statement then puts characters next to eachother to eliminate space left if special character is in original input
    new_that = ''.join(c for c in new_that if c not in '[@!#$%^&*()<>?/|}{~:]')
    # testing to see if the first character of the string is a digit
    if new_that[0].isdigit() == True:
    # if the first index is a digit, return a statement that this is not acceptable to user
        return 'You need to not lead with a digit.'
    # if first index is not a digit returns the now acceptable string
    else:
        return new_that
# Tested against a few different strings with different components of unacceptable circumstances.
normalize_name('2wendy')
normalize_name('   $%torrie23_^')

#11. cumulative_sum, list of numbers and returns list that is cumulative sum of numbers in list
# cumulative_sum has a single input, a list, and outputs a single list
def cumulative_sum(list_nums):
    # creation of a new local list
    new_list = []
    # creation of a new local variable to keep track of cumulative value of input list
    cumulative_total = 0
    # for loop that iterates through the input list
    for i in list_nums:
        # adds the current value to the cumulative_total variable
        cumulative_total += i
        # appends this cumulative_total value to the local list
        new_list.append(cumulative_total) 
    # returns the new_list (local list) values to user
    return new_list
# Tested against some different lists to ensure correct outcome. 
cumulative_sum([1,2,3])
cumulative_sum([1,1,1])




