#!/usr/bin/python3
import sys

#if __name__ == __"main"__

sum = 0
for x in range(1, len(sys.argv)):
    sum += int(sys.argv[x])
print(sum)
