states = {'Ciaro':'CA', 'Alexandria':'AL', 'Giza':'GZ'}
cities = {'CA':'maadi', 'GZ':'dokki'}
print('-' * 25)
for state,abbrev in list(states.items()):
	print(f"{state} is abbreviated {abbrev}")
print('-' * 25)
print(states.items())
state = states.get('Helwan')
if not state:
	print("sorry")