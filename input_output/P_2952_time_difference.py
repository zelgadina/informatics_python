#!/usr/bin/env python

one_h, one_m, one_s = int(input()), int(input()), int(input())
two_h, two_m, two_s = int(input()), int(input()), int(input())

one_all = one_h * 60 * 60 + one_m * 60 + one_s
two_all = two_h * 60 * 60 + two_m * 60 + two_s

print(two_all - one_all)