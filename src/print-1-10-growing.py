
# Print the numbers described in the exercise

number = ''
n = 10

for i in range(1, n+1):
    for j in range(1, i+1):
        if j != i:
            number += '{} '.format(j)
        elif j == i:
            number += '{}'.format(j)
    number += '\n'

print(number.rstrip())
