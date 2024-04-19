------------------
![Albert_Einstein_Head_H3000x1688](https://user-images.githubusercontent.com/49293816/188544854-5ad5a6a8-38df-4cc7-9840-f012a24bc445.jpg)

------------------
## What is Affine Cipher?

as **Wikipedia** says: The affine cipher is a type of monoalphabetic substitution cipher, where each letter in an alphabet is mapped to its numeric equivalent, encrypted using a simple mathematical function, and converted back to a letter.
* look at the entire article from here: https://en.wikipedia.org/wiki/Affine_cipher
## Formula

```
  C = (a * P + b) mod 26
  P = (a ^ -1 * (C - b)) mod 26
```
## Guide
```
 ! Usage: python3 affinecipher.py <type> <string> <a> <b>
  
* type    : {e: encryption, d: decryption}
* string  : the text you want to encrypt or decrypt
* a       : the first operand of the key
* b       : the second operand of the key
```
  
## Contact Me

* [Twitter][_1]

[_1]: https://twitter.com/amait0u
