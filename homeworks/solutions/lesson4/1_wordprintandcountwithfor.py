# open the file
balls_file = open('balls.txt', 'r')

# get the file as unique string
balls_file_string = balls_file.read()

# split the string in an array
balls_file_string = balls_file_string.split()

# set word count
word_count = len(balls_file_string)

# for in range word_count
for i in range(word_count):
    print(i + 1, balls_file_string[i])

# print the word count
print ('The word count is:', word_count)
