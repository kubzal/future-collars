import random

print(random.random())

print(random.randrange(1, 10, step=2))

lst = ["kotlet schabowy", "gołąbki", "pierogi ruskie", "mielone", "naleśniki", "kartacze", "gulasz"]
print(lst)

random.shuffle(lst)
print(lst)

print(random.sample(lst, k=2))