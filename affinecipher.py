import sys
import string
import platform

def gcd(x, y):
    while y:
        x, y = y, x % y
    return x

def are_coprime(a, m):
    return gcd(a, m) == 1

def keyinverse(a, m):
    if not are_coprime(a, m):
        raise ValueError("The 'a' value must be coprime to 26.")
    for i in range(1, m):
        if (a * i) % m == 1:
            return i
    raise ValueError("Inverse does not exist for the given 'a' value.")

def calcenc(c, a, b):
    return (a * c + b) % 26

def calcdec(c, a, b):
    return (keyinverse(a, 26) * (c - b)) % 26

def encryption(p, a, b):
    result = ""
    for char in p:
        if char.isalpha():
            base = lower if char.islower() else upper
            result += base[calcenc(base.index(char), a, b)]
        else:
            result += char
    return result

def decryption(c, a, b):
    result = ""
    for char in c:
        if char.isalpha():
            base = lower if char.islower() else upper
            result += base[calcdec(base.index(char), a, b)]
        else:
            result += char
    return result

if __name__ == "__main__":
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase

    system_platform = platform.system()

    if system_platform == "Linux" or system_platform == "Darwin":
        red, green, yellow, blue, endc = '\033[91m', '\033[92m', '\033[93m', '\033[94m', '\033[0m'
    else:
        red = green = yellow = blue = endc = ""

    if len(sys.argv) < 5:
        print(f"{red}! Usage: {endc}python3 affinecipher.py <type> <string> <a> <b>")
        print('''
        - type    : {e: encryption, d: decryption}
        - string  : the text you want to encrypt or decrypt
        - a       : the first operand of the key
        - b       : the second operand of the key
    ''')
        print(f"{yellow}* Note: {endc}make sure 'a' is coprime to 26 for a valid Affine Cipher")
        print(f"{yellow}* Note: {endc}make sure you add double quotes in case the string has whitespaces")
        exit()

    args = sys.argv
    try:
        a = int(args[3])
        b = int(args[4])

    except ValueError:
        print(f"{red}Error: {endc}Operands must be numbers not strings")
        exit()

    if not are_coprime(a, 26):
        print(f"{red}Error: {endc}The 'a' value must be coprime to 26.")
        exit()

    if args[1] == "e":
        print(encryption(args[2], a, b))
    elif args[1] == "d":
        print(decryption(args[2], a, b))
    else:
        print(f"{red}!Error: {endc}Invalid type of operation")
