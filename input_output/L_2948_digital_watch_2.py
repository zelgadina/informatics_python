#!/usr/bin/env python

num = int(input())
h = num // (60*60) % 24
m = num // 60 % 60
s = num % 60
print(f'{h}:{m:02d}:{s:02d}')