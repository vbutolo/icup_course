# get a string as input
string = input('Insert a string: ')

# initialize result to a empty dictionary
result = {}

# loop through the letters in the string
for letter in string:
    # discard empty spaces
    if letter != ' ':
        # if letter in result keys increase the counter
        if letter in result.keys():
            # increase the counter
            result[letter] += 1
        # else
        else:
            # set the counter to 1
            result[letter] = 1

# print result
print(result)
