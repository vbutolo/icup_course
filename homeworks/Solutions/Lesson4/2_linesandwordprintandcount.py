# open the file
balls_file = open('balls.txt', 'r')

balls_lines_array = balls_file.readlines()

line_count =0
word_count = 0

for i in range(len(balls_lines_array)):
    splitted = balls_lines_array[i].split()
    line_count += 1
    for j in range(len(splitted)):
        print("Line n.", i + 1, ",Word n.", j + 1, ":   " ,splitted[j])
        word_count += 1

print('\n')
print ('The line count is:', line_count)
print ('The word count is:', word_count)
