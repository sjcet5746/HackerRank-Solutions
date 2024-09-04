#Written by Gskd

import re

def change(match):
    value = match.group()
    if value == " && ":
        return " and "
    elif value == " || ":
        return " or "
    else:
        return value
n = int(input())
for i in range(n):
    text = input()
    while ' && ' in text or ' || ' in text:
        text = re.sub(r"\s&&\s|\s\|\|\s",change, text)
    else:
        print(text)
