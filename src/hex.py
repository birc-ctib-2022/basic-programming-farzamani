import sys

# This program should take two arguments, a command--either "encode" or "decode"--
# and then a string.

if len(sys.argv) != 3:
    print("Incorrect number of arguments.", file=sys.stderr)
    print(f"Usage: {sys.argv[0]} command string\n", file=sys.stderr)
    sys.exit(1)

command, x = sys.argv[1:3]

match command:
    case "encode":
        # Implement the encoding here        
        encoding = ""
        for char in x:
            encoding += hex(ord(char))
        print(encoding)

    case "decode":
        # Implement the decoding here
        decoding = ""
        dec = x.split('0x')
        dec = dec[1:]

        for num in dec:
            decoding += chr(int(num, base = 16))

        print(decoding)
