
# You should write a loop around this question, and keep asking until
# the answer is "yes" (lower case).

n = "no"

while n != "yes":
    n = str(input('Do you want to stop? '))
    if n == "yes":
        break
    