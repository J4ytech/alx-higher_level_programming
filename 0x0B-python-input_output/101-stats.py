#!/usr/bin/python3
"""
Module: 101-stats
This script reads stdin line by line and computes metrics.
"""

import sys

def print_stats(size, codes):
    print("File size: {}".format(size))
    for code in sorted(codes.keys()):
        if codes[code] > 0:
            print("{}: {}".format(code, codes[code]))

size = 0
codes = {200:0, 301:0, 400:0, 401:0, 403:0, 404:0, 405:0, 500:0}
count = 0

try:
    for line in sys.stdin:
        parts = line.split()
        if len(parts) >= 2:
            try:
                size += int(parts[-1])
            except ValueError:
                pass
            try:
                code = int(parts[-2])
                if code in codes:
                    codes[code] += 1
            except ValueError:
                pass
        count += 1
        if count % 10 == 0:
            print_stats(size, codes)
except KeyboardInterrupt:
    pass
finally:
    print_stats(size, codes)
