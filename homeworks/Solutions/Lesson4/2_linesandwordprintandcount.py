# open the file
balls_file = open('balls.txt', 'r')

# get the file as array of lines
balls_lines_array = balls_file.readlines()

# initialite line_count and word_count to
line_count =0
word_count = 0

# for i in lines
for i in range(len(balls_lines_array)):
    
    # define splitted as array of words of a single line
    splitted = balls_lines_array[i].split()

    # increment line_count by one
    line_count += 1

    # for j in words of lines
    for j in range(len(splitted)):

        # print line number and word number
        print("Line n.", i + 1, ",Word n.", j + 1, ":   " ,splitted[j])
        
        # increment word_count by one
        word_count += 1

# print results
print('\n')
print ('The line count is:', line_count)
print ('The word count is:', word_count)
