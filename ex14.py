from sys import argv
script , user_name = argv
prompt = '> '
print(f"Hi {user_name}, i'm the {script} script.")
print("i'd like to ask you a few questions.")
print(f"Do you like owls, {user_name}?")
likes = input(prompt)
print(f"Where do you live, {user_name}?")
lives = input(prompt)
print(f"What kind of computer do you have, {user_name}?")
computer = input(prompt)
print(f"""Alright, so you {likes} Owls.
	You live in {lives}, you have a {computer}.
	great!""")