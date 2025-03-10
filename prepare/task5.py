numbers = list(map(int, input().split()))


def is_even(n: int) -> bool:
    return n % 2 == 0


even_numbers = list(filter(is_even, numbers))
print(even_numbers)
