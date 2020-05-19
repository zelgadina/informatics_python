#!/usr/bin/env python

a, b, n = int(input()), int(input()), int(input())
buy = ((a * 100) + b) * n
print(buy // 100, buy % 100)