# 1. A. (Done in terminal)
# import function_exercises as func
# func.is_vowel('a')

# 1. B. import tip_calculator using from
from function_exercises import calculate_tip
print(calculate_tip(.3, 100))

# 1. C. Notebook file
# 2. A. itertools
import itertools as i
x = i.product("abc", [1, 2, 3])
print(list(x))
# When using the product function produces 9 results.
print(list(i.combinations("abcd", 2)))
# There are 6 unique combinations produced.
print(list(i.permutations("abcd", 2)))
# There are 12 unique permutations produced.

import json
profiles = json.load(open('profiles.json'))
# Total number of users
user_count = len(profiles)
print(user_count)
# Alters the data in the balance key in my copied dict profiles, returns
# list of balances
def balance_list(d):
    balances = []
    for x in d:
        x['balance'] = x['balance'].replace('$', '')
        x['balance'] = x['balance'].replace(',', '')
        x['balance'] = float(x['balance'])
        balances.append(x['balance'])
    return balances
# Have a list of balances, that are now floats (and are floats in the dict profiles)
balances_list = balance_list(profiles)
print(balances_list)
# Number of active users/inactive users
def count_active(d):
    count = 0
    for x in d:
        if x['isActive'] == True:
            count += 1
    return count 
count_total = count_active(profiles)
print(count_total)
# Total number of active users is 9
def count_inactive(d):
    count = 0
    for x in d:
        if x['isActive'] == False:
            count += 1
    return count 
count_total_inact = count_inactive(profiles)
print(count_total_inact)
# Total number of inactive users is 10 (negation of above)

# Total of balances
def balance_total(l):
    total = 0
    for i in l:
        total += i
    return total
total_bal = balance_total(balances_list)
print(total_bal)
# The total balance 52,667.02

# Average balance per user
avg_balance = total_bal / user_count 
print(avg_balance)
# 2771.948 for avg balance

# User with the lowest balance
def lowest_bal(bal_list):
    lowbals = []
    minimum = min(bal_list)
    for i in range(len(bal_list)):
        if bal_list[i] == minimum:
            lowbals.append(i)
    names = []
    for n in range(len(lowbals)):
        x = lowbals[n]
        names.append(profiles[x]['name'])
    return names    
print(lowest_bal(balances_list))
# Avery Flynn is the user (sole user) with the minimum balance

# User with the highest balance
def highest_bal(bal_list):
    highbals = []
    maximum = max(bal_list)
    for i in range(len(bal_list)):
        if bal_list[i] == maximum:
            highbals.append(i)
    names = []
    for n in range(len(highbals)):
        x = highbals[n]
        names.append(profiles[x]['name'])
    return names    
print(highest_bal(balances_list))
# Fay Hammond is the user (sole user) with the maximum balance

# Most common favorite fruit
def favorite_fruit_list(d):
    fav_fruits = []
    for i in d:
        fav_fruits.append(i['favoriteFruit'])
    return fav_fruits
fruit_list = favorite_fruit_list(profiles)
print(fruit_list)

def most_frequent(listylist):
    return max(set(listylist), key = listylist.count)
fruityfruit = most_frequent(fruit_list)
print(fruityfruit)
# The most common favorite fruit is strawberry.

# Least common favorite fruit
def least_frequent(listylist):
    return min(set(listylist), key = listylist.count)
fruityfruit2 = least_frequent(fruit_list)
print(fruityfruit2)
# The least common favorite fruit is apple.

# Total number of unread messages for all users
def unread_total(d):
    total = 0
    for i in d:
        total += int(''.join(x for x in i['greeting'] if x.isdigit()))
    return total
unread_total(profiles)
# There are a total of 210 unread messages. 





