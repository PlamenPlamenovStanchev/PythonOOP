from math import sqrt

def get_primes(numbers):
    for number in numbers:
        if number < 2:
            continue
        # for i in range(2, number):
        for i in range(2, int(sqrt(number)) + 1):
            if number % i == 0:
                break
        else:
            yield number
