import bleach

str = input("Enter a string: ")
#
# need to save the output of clean to a variable
#
sanatized_string = bleach.clean(str)
#
# print unsantized output
#
print(str)
#
# print the input as sanatized output
#
print(sanatized_string)