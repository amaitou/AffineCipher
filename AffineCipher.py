import sys
import string
import platform

"""
    Affine Cipher Implementation
    ----------------------------
        This script provides an implementation of the Affine Cipher, a type of substitution cipher
        that combines modular arithmetic for encryption and decryption. The script includes functions
        for calculating the greatest common divisor, checking coprimality, and finding modular inverses.
        It defines separate functions for encryption and decryption operations. The command-line interface
        allows users to specify the type of operation (encryption 'e' or decryption 'd'), the input string,
        and the key parameters 'a' and 'b'. The script includes error handling to ensure valid input, such as
        verifying that the 'a' parameter is coprime to 26. Additionally, the script adapts the output color
        formatting based on the platform, providing enhanced readability on Linux and macOS terminals.
"""

def gcd(x, y):
    """
        gcd(x, y) -> int
        Calculates the greatest common divisor of two integers using the Euclidean algorithm.
        Returns the computed GCD.
    """
    while y:
        x, y = y, x % y
    return x

def are_coprime(a, m):
    """
        are_coprime(a, m) -> bool
        Checks if two integers 'a' and 'm' are coprime (have a GCD of 1).
        Returns True if coprime, False otherwise.
    """
    return gcd(a, m) == 1

def keyinverse(a, m):
    """
        keyinverse(a, m) -> int
        Finds the modular inverse of 'a' modulo 'm' if 'a' is coprime to 'm'.
        Raises a ValueError if the inverse does not exist.
        Returns the computed modular inverse.
    """
    if not are_coprime(a, m):
        raise ValueError("The 'a' value must be coprime to 26.")
    for i in range(1, m):
        if (a * i) % m == 1:
            return i
    raise ValueError("Inverse does not exist for the given 'a' value.")

def calcenc(c, a, b):
    """
        calcenc(c, a, b) -> int
        Performs encryption for a single character using the Affine Cipher formula.
        Returns the encrypted character's index in the alphabet.
    """
    return (a * c + b) % 26

def calcdec(c, a, b):
    """
        calcdec(c, a, b) -> int
        Performs decryption for a single character using the Affine Cipher formula.
        Returns the decrypted character's index in the alphabet.
    """
    return (keyinverse(a, 26) * (c - b)) % 26

def encryption(p, a, b):
    """
        encryption(p, a, b) -> str
        Encrypts a given plaintext using the Affine Cipher with specified key parameters 'a' and 'b'.
        Returns the encrypted ciphertext.
    """
    result = ""
    for char in p:
        if char.isalpha():
            base = lower if char.islower() else upper
            result += base[calcenc(base.index(char), a, b)]
        else:
            result += char
    return result

def decryption(c, a, b):
    """
        decryption(c, a, b) -> str
        Decrypts a given ciphertext using the Affine Cipher with specified key parameters 'a' and 'b'.
        Returns the decrypted plaintext.
    """
    result = ""
    for char in c:
        if char.isalpha():
            base = lower if char.islower() else upper
            result += base[calcdec(base.index(char), a, b)]
        else:
            result += char
    return result

if __name__ == "__main__":
    """
        Command-Line Interface
        Parses command-line arguments, performs input validation, and executes encryption or
        decryption based on user input. Provides informative error messages and usage instructions.
    """
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
