#!/usr/bin/env python3

from Crypto.Cipher import XOR

def main():
  key = b"The secret key"

  # Encryption
  encryption_suite = XOR.new(key)
  cipher_text = encryption_suite.encrypt(b"Hello world!")
  print(cipher_text)

  # Decryption
  decryption_suite = XOR.new(key)
  plain_text = decryption_suite.decrypt(cipher_text)
  print(plain_text)

  # Crack
  crack_suite = XOR.new(plain_text)
  key = crack_suite.encrypt(cipher_text)
  print(key)

if __name__ == '__main__':
  main()
