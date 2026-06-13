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


def sieve_primes(start, end):
    if not isinstance(start, int) or not isinstance(end, int):
        raise TypeError("输入必须为整数")
    if start > end:
        raise ValueError("起始值不能大于结束值")
    if end < 2:
        return []
    start = max(start, 2)
    if end < 3:
        return [2] if start <= 2 else []
    limit = math.isqrt(end)
    base = [True] * (limit + 1)
    base[0] = base[1] = False
    for i in range(2, limit + 1):
        if base[i]:
            for j in range(i * i, limit + 1, i):
                base[j] = False
    small_primes = [i for i, is_p in enumerate(base) if is_p]
    size = end - start + 1
    sieve = [True] * size
    for p in small_primes:
        first = max(p * p, ((start + p - 1) // p) * p)
        for j in range(first - start, size, p):
            sieve[j] = False
    return [start + i for i, is_p in enumerate(sieve) if is_p]


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
