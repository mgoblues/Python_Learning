'''for the intergers 1 through 50, find the sum of even numbers minus the sum of numbers that are divisible by 7:

Need to:
	-define range of intergers 1-50
	-define even intergers
	-sum even intergers
	-define intergers divisible by 7
	-sum intergers divisible by 7
	-subtract even intergers from /7 intergers'''


def get_first_fifty():
	'''Get a list of intergers 1-50, returning to new list'''
	return list(range(1,51))

intergers = get_first_fifty()
print(intergers)

def is_even(intergers):
	'''Filter out intergers that are even from 1-50'''
	even = []
	for number in intergers:
		if number % 2 == 0:
			even.append(intergers) 
	return even	

print(is_even(get_first_fifty()))


#def sum_of_even():
#	'''Filter out even intergers (divisble by 2)'''
#	sig_even = sum(is_even(get_first_fifty))	
#	return sig_even

#print(sum_of_even)
