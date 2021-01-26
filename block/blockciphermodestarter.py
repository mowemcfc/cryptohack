#!/usr/bin/env python3

import requests
import json

ct = "e59c42a9b5bfa13b6267903565586137000289b52a5a0ee6a6139d6efe374ad6"

resp = requests.get(f"http://aes.cryptohack.org/block_cipher_starter/decrypt/{ct}")

print(bytes.fromhex(json.loads(resp.text)["plaintext"]).decode("ASCII"))


