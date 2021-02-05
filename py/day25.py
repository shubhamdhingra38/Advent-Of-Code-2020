a = 1965712
b = 19072108
MOD = 20201227
k1 = 0
while True:
    if pow(7, k1, MOD) == a:
        break
    k1 += 1

print(k1)

k2 = 0
while True:
    if pow(7, k2, MOD) == b:
        break
    k2 += 1

print(k2)

print(pow(7, k1, MOD))

"""
7779516
7177897
"""