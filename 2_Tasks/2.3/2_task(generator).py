def primes():
    value = 1
    while True:
        counter = 0
        value += 1
        for i in range(2, value):
            if value % i == 0:
                counter += 1
        if counter < 1:
            yield value


gen = primes()

next(gen)


