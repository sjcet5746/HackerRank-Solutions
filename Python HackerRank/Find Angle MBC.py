#Written by Gskd
import math

ab = float(input())
bc = float(input())

ac = math.sqrt((ab*ab)+(bc*bc))
bm = ac / 2.0
mc = bm

b = mc
c = bm
a = bc

angel_b_radian = math.acos(a / (2*b))

angel_b_degree = int(round((180 * angel_b_radian) / math.pi))

print(angel_b_degree,'\u00B0',sep='')
