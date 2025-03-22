def factorial(n):
    """Zwraca silnię liczby całkowitej n."""
    if n < 0:
        raise ValueError("Liczba musi być nieujemna")
    return 1 if n == 0 else n * factorial(n - 1)
