
# Print the numbers described in the exercise

number = ''
n = 10

for i in range(1, n+1):
    for j in range(1, i+1):
        number += '{} '.format(j)
        # print(j,end=' ')
    number += '\n'

print(number.strip())
