from itertools import count
from itertools import cycle

for num in count(3):
    if num > 10:
        break
    else:
        print(num)

c = 0
for el in cycle("GEEK"):
    if c > 11:
        break
    print(el)
    c += 1
