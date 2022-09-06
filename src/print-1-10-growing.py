
# Print the numbers described in the exercise

number = ''
n = 10

for i in range(1, n+1):
    for j in range(1, i+1):
        number += '{} '.format(j)
    if i < 10:
        number += '\n'

print(number.rstrip())
