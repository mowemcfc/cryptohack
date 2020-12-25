#!/usr/bin/python3

from Crypto.Util.number import long_to_bytes, bytes_to_long
import sys
import textwrap
def main(ct):
    b = long_to_bytes(ct)
    print(b)


if __name__ == "__main__":
    ct = sys.argv[1]
    main(ct)
