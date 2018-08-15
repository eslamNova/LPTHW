#like argv
def print_two(*args):
	arg1 , arg2 = args
	print(f"arg1: {arg1}, arg2: {arg2}.")
#another way
def print_two_agian(arg1, arg2):
	print(f"arg1: {arg1}, arg2: {arg2}.")
#one arg
def print_one(arg1):
	print(f"arg1: {arg1}.")
#none
def print_none():
	print("i got nothin")
print_two("alien", "moon")
print_two_agian("islam", "owls")
print_one("moon")
print_none()