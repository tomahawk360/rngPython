import time

def Lehmer(num):
    m = 2147483647
    a = 48271

    q = m / a
    r = m % a

    seed = int(time.time()) % m

    for i in range(num):
        t = a * (seed % q)
        s = r * (seed / q)
        ts = t - s

        if ts > 0:
            seed = ts
        else:
            seed = ts + m

    return float(seed) / m

nene = int(input("Ingrese numero de iteraciones:"))
print(Lehmer(nene))