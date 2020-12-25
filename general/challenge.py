#!/usr/bin/python3
from Crypto.Util.number import long_to_bytes, bytes_to_long
import sys
import textwrap
import json
import codecs
import base64
from pwn import *

HOST = "socket.cryptohack.org"
PORT = 13377


def json_send(s, r):
    request = json.dumps(r).encode()
    print(request)
    s.sendline(request)
    return

def b64(encoded):
    decoded = base64.b64decode(encoded).decode()
    return decoded

def bigint(encoded):
    decoded = long_to_bytes(int(encoded, 16)).decode()
    return decoded

def decodehex(encoded):
    decoded = "".join([chr(int(h, 16)) for h in textwrap.wrap(encoded,2)])
    return decoded

def utf8(encoded):
    decoded = "".join([chr(b) for b in encoded])
    return decoded

def rot13(encoded):
    decoded = codecs.decode(encoded, "rot_13")
    return decoded

def main():

    request = {
            "decoded": ""
    }

    s = remote(HOST, PORT)
    while True:
        msg = s.recvline().decode()
        print(msg)
        msg_json = json.loads(msg)
        enc_type = msg_json["type"]
        encoded = msg_json["encoded"]
        print(enc_type)

        if enc_type == "bigint":
            decoded = bigint(encoded)
            request["decoded"] = decoded
            print(decoded)
            json_send(s, request)
        if enc_type == "base64":
            decoded = b64(encoded)
            print(decoded)
            request["decoded"] = decoded
            json_send(s, request)
        if enc_type == "hex":
            decoded = decodehex(encoded)
            request["decoded"] = decoded
            print(decoded)
            json_send(s, request)
        if enc_type == "utf-8":
            decoded = utf8(encoded)
            request["decoded"] = decoded
            print(decoded)
            json_send(s, request)
        if enc_type == "rot13":
            decoded = rot13(encoded)
            request["decoded"] = decoded
            print(decoded)
            json_send(s, request)

        

main()
