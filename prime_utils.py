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
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


def get_factors(n):
    if not isinstance(n, int):
        raise TypeError("输入必须为整数")
    if n <= 0:
        raise ValueError("输入必须为正整数")
    factors = set()
    for i in range(1, int(math.isqrt(n)) + 1):
        if n % i == 0:
            factors.add(i)
            factors.add(n // i)
    return sorted(factors)


def prime_factors(n):
    if not isinstance(n, int):
        raise TypeError("输入必须为整数")
    if n <= 1:
        raise ValueError("输入必须大于1")
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n = n // 2
    i = 3
    while i * i <= n:
        while n % i == 0:
            factors.append(i)
            n = n // i
        i += 2
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
