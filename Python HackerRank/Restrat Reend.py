#Written by Gskd

import re

s, k = input(), input()

idx = [(m.start(1), m.end(1) -1) for m in re.finditer(fr"(?=({k}))", s)]

print(*idx or [(-1, -1)], sep="\n")
