# Making a list of alphabets

alphabets = 'abcdefghijklmnopqrstuvwxyz'
lsit_alph = list(alphabets)

# Making a list of letters in the input value
in_str = str(input('Enter a sentence: ').replace(' ','').lower())
list_in_str =list(in_str)


# Checking if the input letters contain all the 26 aplhabets 
count = 0

for m in lsit_alph:
    if m in list_in_str:
        count+= 1

if count == 26:
    print('This string is a panagram.')
else:
    print('This string is not a panagram.')
