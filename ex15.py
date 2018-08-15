from sys import argv
#add argv
script , file_name = argv 
#open file
txt = open(file_name)
print(f"here is your file {file_name}.")
#use file functions to read file
print(txt.read())
txt.close()
print("Type the filename again: ")
file_again = input('>>> ')
txt_again = open(file_again)
print(txt_again.read())
txt_again.close()