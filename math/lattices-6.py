#!/usr/bin/python3
from sage.all import *
from Crypto.Util.number import getPrime, inverse, bytes_to_long, long_to_bytes
import random
import math

FLAG = b'crypto{?????????????????????}'


def gen_key():
    q = getPrime(512)
    upper_bound = int(math.sqrt(q // 2))
    lower_bound = int(math.sqrt(q // 4))
    f = random.randint(2, upper_bound)
    while True:
        g = random.randint(lower_bound, upper_bound)
        if math.gcd(f, g) == 1:
            break
    h = (inverse(f, q)*g) % q
    return (q, h), (f, g)


def encrypt(q, h, m):
    assert m < int(math.sqrt(q // 2))
    r = random.randint(2, int(math.sqrt(q // 2)))
    e = (r*h + m) % q
    return e


def decrypt(q, h, f, g, e):
    a = (f*e) % q
    m = (a*inverse(f,g)) % g
    return m


public, private = gen_key()
q, h = 7638232120454925879231554234011842347641017888219021175304217358715878636183252433454896490677496516149889316745664606749499241420160898019203925115292257, 2163268902194560093843693572170199707501787797497998463462129592239973581462651622978282637513865274199374452805292639586264791317439029535926401109074800
f, g = private

m = bytes_to_long(FLAG)
e = 5605696495253720664142881956908624307570671858477482119657436163663663844731169035682344974286379049123733356009125671924280312532755241162267269123486523

f = 47251817614431369468151088301948722761694622606220578981561236563325808178756
g = 43997957885147078115851147456370880089696256470389782348293341937915504254589

m = decrypt(q, h, f, g, e)
m = str(long_to_bytes(m))
print(m)

print(f'Public key: {(q,h)}')
print(f'Encrypted Flag: {e}')
