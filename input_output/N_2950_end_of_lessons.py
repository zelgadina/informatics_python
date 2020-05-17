#!/usr/bin/env python

num = int(input())
end = 525 + (num * 50 + ((num + 1) // 2) * 10)
print(end // 60, end % 60)