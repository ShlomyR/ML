'''for i in range(1,11):
	print(i)'''


'''numbers = list(range(1,6))
print(numbers)'''

'''name = input("How old are you sun? ")
age = int(name)
while age >= 18:
	print("You are old enough to vote!")
	or age > 120:
		print("come on bro, get out of here!")
	break
if age < 18:
	print("Sorry sun you'r not old enough to vote!")
#elif age > 120:
#	print("come on bro, get out of here!")'''
'''requested_toppings1 =input("What toppings do you like kinde sir? ")
#requested_toppings = ['mushrooms', 'extra cheese']
if 'mushrooms' in requested_toppings1:
	print("Adding mushrooms.")
if 'pepperoni' in requested_toppings1:
	print("Adding pepperoni.")
if 'extra cheese' in requested_toppings1:
	print("Adding extra cheese.")

print("\nFinished making your pizza!")'''


'''available_toppings = ['mushrooms', 'olives', 'green peppers', 'pepperoni', 'pineapple', 'extra cheese']

requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

for requested_topping in requested_toppings:
	if requested_topping in available_toppings:
		print("Adding " + requested_topping + ".")
	else:
		print("Sorry, we don't have " + requested_topping + ".")

print("\nFinished making your pizza!")'''

'''alien_0 = {'color': 'green', 'points': 5}
print(alien_0['color'])
print(alien_0['points'])'''



'''def describe_pet(animal_type = 'pizaa', pet_name = 'harry'):
 """Display information about a pet."""
 print("\nI have a " + animal_type + ".")
 print("My " + animal_type + "'s name is " + pet_name.title() + ".")

describe_pet(animal_type = 'pi', pet_name = 'har')'''


'''def get_formatted_name(first_name, last_name):
 """Return a full name, neatly formatted."""
 full_name = first_name + ' ' + last_name
 return full_name.title()
musician = get_formatted_name('jimi', 'hendrix')
print(musician)'''



'''def get_formatted_name(first_name, last_name, middle_name=''):
	"""Return a full name, neatly formatted."""
	if middle_name:
		full_name = first_name + ' ' + middle_name + ' ' + last_name
	else:
		full_name = first_name + ' ' + last_name

	return full_name.title()


musician = get_formatted_name('jimi', 'hendrix')
print(musician)

musician = get_formatted_name('john', 'hooker', 'lee')
print(musician)'''

def get_formatted_name(first_name, last_name):
	"""Return a full name, neatly formatted."""
	full_name = first_name + ' ' + last_name
	return full_name.title()

# This is an infinite loop!
while True:
	print("\nPlease tell me your name:")
	f_name = input("First name: ")
	l_name = input("Last name: ")
	break
formatted_name = get_formatted_name(f_name, l_name)
print("\nHello, " + formatted_name + "!")
