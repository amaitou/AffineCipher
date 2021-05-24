
## What is Affine Cipher ?

as **wikipedia** says : The affine cipher is a type of monoalphabetic substitution cipher, where each letter in an alphabet is mapped to its numeric equivalent, encrypted using a simple mathematical function, and converted back to a letter.
* look at the entire article from here : https://en.wikipedia.org/wiki/Affine_cipher
## Formula

```
  C = (a * P + b) mod 26
  P = (a ^ -1 * (C - b)) mod 26
```
## Guide

 Usage: python3 affinecipher.py <type> <string> <a> <b>
  
* type    : {e: encryption, d: decryption}
* string  : the text you want to enrypt or decrypt
* a       : the first operand of the key
* b       : the second operand of the key
  
## Contact Me
  
* Facebook : https://www.facebook.com/Lelouche01/
* Twitter : https://twitter.com/Lelouche01
* Github : https://github.com/Lelouche01
