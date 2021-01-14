from itertools import combinations
import requests
from functools import reduce
import operator
import gmpy2
from Crypto.Util import number

resp = requests.get('https://cryptohack.org/static/challenges/output_0ef6d6343784e59e2f44f61d2d29896f.txt')

lines = resp.text.splitlines()

params = []

for i in range(0, len(lines), 5):
    n = int(lines[i].split(' ')[-1])
    e = int(lines[i+1].split(' ')[-1])
    c = int(lines[i+2].split(' ')[-1])
    params.append([n, c])

def solve(ns, cs):
    M = reduce(operator.mul, ns)
    Mi = [M//n for n in ns]
    ti = [pow(Mi, -1, n) for Mi, n in zip(Mi, ns)]
    x = sum([c*t*m for c, t, m in zip(cs, ti, Mi)]) % M
    r, exact = gmpy2.iroot(x, 3)
    if exact:
        return r

for cb in combinations(params, 3):
    ns = [x[0] for x in cb]
    cs = [x[1] for x in cb]
    r = solve(ns, cs)
    if r == None:
        continue
    print(number.long_to_bytes(r))
