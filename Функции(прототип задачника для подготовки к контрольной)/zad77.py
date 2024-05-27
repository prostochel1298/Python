def all_divisors(number):
    i = 1
    a = []
    while i ** 2 <= number:
        if number % i == 0:
            a.append(i)
            if i != number // i:
                a.append(number // i)
        i += 1
    a.sort()
    print(a)

all_divisors(6000000000)