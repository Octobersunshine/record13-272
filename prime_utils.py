import math


def is_prime(n):
    if not isinstance(n, int):
        raise TypeError("输入必须为整数")
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    limit = math.isqrt(n)
    i = 5
    while i <= limit:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


def get_factors(n):
    if not isinstance(n, int):
        raise TypeError("输入必须为整数")
    if n <= 0:
        raise ValueError("输入必须为正整数")
    pf = prime_factors(n)
    counter = {}
    for p in pf:
        counter[p] = counter.get(p, 0) + 1
    divisors = [1]
    for prime, exp in counter.items():
        new_divisors = []
        pe = 1
        for e in range(exp + 1):
            for d in divisors:
                new_divisors.append(d * pe)
            pe *= prime
        divisors = new_divisors
    return sorted(divisors)


def prime_factors(n):
    if not isinstance(n, int):
        raise TypeError("输入必须为整数")
    if n <= 1:
        raise ValueError("输入必须大于1")
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n = n // 2
    while n % 3 == 0:
        factors.append(3)
        n = n // 3
    limit = math.isqrt(n)
    i = 5
    while i <= limit:
        while n % i == 0:
            factors.append(i)
            n = n // i
        while n % (i + 2) == 0:
            factors.append(i + 2)
            n = n // (i + 2)
        limit = math.isqrt(n)
        i += 6
    if n > 2:
        factors.append(n)
    return factors


def analyze_number(n):
    if not isinstance(n, int):
        raise TypeError("输入必须为整数")
    result = {
        "number": n,
        "is_prime": is_prime(n),
        "factors": get_factors(n) if n > 0 else [],
        "prime_factors": prime_factors(n) if n > 1 else []
    }
    return result
