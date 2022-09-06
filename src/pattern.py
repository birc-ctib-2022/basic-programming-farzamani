
# Print the pattern

n = 5

for i in range(1, n+1):
    for j in range(1, i+1):
        print("*",end=' ')
    print('').strip()

for i in reversed(range(1, n)):
    for j in reversed(range(1, i+1)):
        print("*",end=' ')
    print('').strip()
