mermaid = 3
bear = 5
hercules = 1
total_cost = 3 * (mermaid + bear + hercules)
print(total_cost)

google = 400
amazon = 380
facebook = 350 
payment_total = (10 * facebook) + (6 * google) + (4 * amazon)
print(payment_total)

class_full = False
schedule_conflict = True
enrolled = class_full and schedule_conflict
print(enrolled)

num_items_bought = 1
prem_member = True
offer_expired = False 
if offer_expired != True:
    num_items_bought > 2 or prem_member
    discount = True
else:
    discount = False
print(discount)

username = 'codeup'
password = 'notastrongpassword'
pass_length = len(password) > 5
user_length = len(username) < 20
same_test = username != password
user_whitespace = username != username.strip()
pass_whitespace = password != password.strip()
print(f"{pass_length}, {user_length}, {same_test}, {user_whitespace}, {pass_whitespace}")

