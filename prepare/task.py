import math

p = 5
kv = 20

need_vse = int(input())

need_p = math.ceil(float(need_vse / kv))
need_s = need_vse - ((need_p - 1) * 20)

need_e = math.ceil(float(need_s / 4))

print(need_p, need_e)
