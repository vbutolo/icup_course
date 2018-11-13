# open the file
balls_file = open('balls.txt', 'r')

# get the file as unique string
balls_file_string = balls_file.read()

# split the string in an array
balls_file_string = balls_file_string.split()

# get the total number of items in the array
counter = len(balls_file_string)

# initialize word count
word_count = 0

# while counter is true
while counter:
    print(word_count + 1, balls_file_string[word_count])
    counter -= 1
    word_count += 1

# formatting
print('\n')

# print the word count
print ('The word count is:', word_count)
