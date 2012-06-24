#!/usr/bin/python
import sys

def nextChar(c):
    return chr( ord(c)+1 )

def cryptalpha(plainword):
    plainword = plainword.lower()
    
    cipherword = ''
    next = 'a'
    map = {}
    
    for c in plainword:
        if c not in map: 
            map[c] = next
            next = nextChar(next)
        cipherword += map[c]
    
    return cipherword

sys.argv = sys.argv[1:]
for arg in sys.argv:
    print '%s=%s' % (arg, cryptalpha(arg))
    
lines = sys.stdin.readlines()
lines = map(lambda x : x[:-1], lines)
for line in lines:
    print '%s=%s' % (line, cryptalpha(line))