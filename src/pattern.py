
# Print the pattern

pattern = ''
n = 5

for i in range(1, n+1):
    for j in range(1, i+1):
        if j != i:
            pattern += "* "
        elif j == i:
            pattern += "*"
    pattern += '\n'

for i in reversed(range(1, n)):
    for j in reversed(range(1, i+1)):
        if j != 1:
            pattern += "* "
        elif j == 1:
            pattern += "*"
    pattern += '\n'

print(pattern.rstrip())
