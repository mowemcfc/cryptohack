#!/usr/bin/env python3

import requests
import textwrap

BASE_URL = "https://aes.cryptohack.org"
CHALL_URL = "/bean_counter/encrypt/"

raw_img = requests.get(f"{BASE_URL}{CHALL_URL}").json()["encrypted"]
raw_img_bytes = bytes.fromhex(raw_img)

keystream = "73ff59679fc3cb59b84ec12e5ae6b749" # xor first 16 bytes of common PNG format w/ bytes of ct

blocks = textwrap.wrap(raw_img,32)
block_size = 16

with open("bean_flag.png", "wb") as f:
    for block in blocks:
        xored = [a^b for a,b in zip(bytes.fromhex(block), bytes.fromhex(keystream))]
        f.write(bytes(xored))
