#!/usr/bin/env python

num = int(input())

hours = num // 60 % 24
mins = num % 60

print(hours, mins)