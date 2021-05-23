
## What is Affine Cipher ?
as **wikipedia** says : The affine cipher is a type of monoalphabetic substitution cipher, where each letter in an alphabet is mapped to its numeric equivalent, encrypted using a simple mathematical function, and converted back to a letter.
* look at the entire article from here : https://en.wikipedia.org/wiki/Affine_cipher
## Formula
```
  C = (a * P + b) mod 26
  P = a ^ -1 * (C - b) mod 26
```
