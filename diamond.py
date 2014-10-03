#!usr/bin/env python
'''
print a diamond with *
'''

N = 10

print " " * (N-1) + "* "
for n in range(2, N):
    print " " * (N-n) + "* " + "  " * (n-2) + "* "
for n in range(N-1):
    print " " * n + "* " + "  " * (N - n - 2) + "* "
print " " * (N-1) + "* "
