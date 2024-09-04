#Written by Gskd
import math
import os
import random
import re
import sys
from datetime import date, time, datetime

def time_delta(t1, t2):

    date_format = "%a %d %b %Y %H:%M:%S %z"

    dt1 = datetime.strptime(t1, date_format)
    dt2 = datetime.strptime(t2, date_format)

    delta_seconds = int(abs(dt1-dt2).total_seconds())

    return str(delta_seconds)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        t1 = input()

        t2 = input()

        delta = time_delta(t1, t2)

        fptr.write(delta + '\n')

    fptr.close()
