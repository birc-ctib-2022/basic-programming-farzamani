import sys

if len(sys.argv) != 2:
    print(f"{sys.argv[0]} expected exactly one argument.")
    sys.exit(1)

password = sys.argv[1]
is_valid = False

# Do all the requirement checks here.

pass_check = {
    "rule 1" : 0, # uppercase
    "rule 1b": 0, # lowercase
    "rule 2" : 0, # numeric
    "rule 3" : 0, # character
    "rule 4" : 0, # len >= 6 
    "rule 5" : 0  # len <= 16
}

if len(password) >=6:
    pass_check["rule 4"] = 1

if len(password) <= 16:
    pass_check["rule 5"] = 1

for x in password:
    if x.isupper() == True:
        pass_check["rule 1"] = 1
    elif x.islower() == True:
        pass_check["rule 1b"] = 1
    elif x.isnumeric() == True:
        pass_check["rule 2"] = 1
    elif x in "$#@":
        pass_check["rule 3"] = 1

is_valid = 0 not in pass_check.values()

print(is_valid)
