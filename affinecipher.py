
import sys
import string
import platform

calcenc = lambda c, a, b: (a * c + b) % 26
calcdec = lambda c, a, b: (keyinverse(a, 26) * (c - b)) % 26

def keyinverse(a, m) :
    for i in range(1, m) :
        if (((a % m) * (i % m)) % m == 1) :
            return i
    return -1 ;

def encryption(p, a, b) :
    c = ""
    for i in p :
        if i.isalpha() :
            if i in lower :
                c += lower[calcenc(lower.index(i), a, b)]
            else :
                c += upper[calcenc(upper.index(i), a, b)]
        else :
            c += i
    return c

def decryption(c, a, b) :
    p = ""
    for i in c :
        if i.isalpha() :
            if i in lower :
                p += lower[calcdec(lower.index(i), a, b)]
            else :
                p += upper[calcdec(upper.index(i), a, b)]
        else :
            p += i
    return p

if __name__ == "__main__" :

    lower = string.ascii_lowercase
    upper = string.ascii_uppercase  

    if platform.system().startswith("Linux") :
	    red , green , yellow , blue , endc = '\033[91m' , '\033[92m' ,'\033[93m' , '\033[94m' , '\033[0m'
    else :
	    red = green = yellow = blue = endc = ""

    if len(sys.argv) < 5 :

        print(red + "! Usage: " + endc + "python3 affinecipher.py <type> <string> <a> <b>")
        print('''
        - type    : {e: encryption, d: decryption}
        - string  : the text you want to enrypt or decrypt
        - a       : the first operand of the key
        - b       : the second operand of the key
    ''')

        print(yellow + "* Note: " + endc + "make sure you add double quotes in case the string has whitespaces")
        exit()
    
    args= [i for i in sys.argv]
    try :
        a = int(args[3])
        b = int(args[4])
    
    except :
        print(red + 'Error: ' + endc + 'Operands must be numbers not strings')
        exit()

    if args[1] == "e" :
        print(encryption(args[2], a, b))
    elif args[1] == "d" :
        print(decryption(args[2], a, b))
    else :
        print(red + "!Error: " + endc + "Unvalid type of operation")
