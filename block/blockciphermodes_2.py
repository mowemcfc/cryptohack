#!/usr/bin/env python3
from Crypto.Cipher import AES
import hashlib
import random
def decrypt(ciphertext, password_hash):
    ciphertext = bytes.fromhex(ciphertext)
    key = password_hash

    cipher = AES.new(key, AES.MODE_ECB)
    try:
        decrypted = cipher.decrypt(ciphertext)
    except ValueError as e:
        return {"error": str(e)}

    return decrypted

def main(ct):

    with open("/usr/share/dict/words") as f:
        words = [w.strip() for w in f.readlines()]

    for word in words:
        word = word.strip()
        hashed = hashlib.md5(word.encode()).digest()
        decrypted = decrypt(ct, hashed)
        print(decrypted)


if __name__ == "__main__":
    ct = "c92b7734070205bdf6c0087a751466ec13ae15e6f1bcdd3f3a535ec0f4bbae66"
    print(main(ct))
