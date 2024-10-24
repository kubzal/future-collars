def simple_generator():
    yield 1
    yield 2
    yield 3


gen = simple_generator()

for value in gen:
    print(value)

gen2 = simple_generator()

print(next(gen2))
print(next(gen2))
print(next(gen2))
