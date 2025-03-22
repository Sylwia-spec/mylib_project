# Link do repozytorium na github.com
# https://github.com/Sylwia-spec/mylib_project

def add(a: int, b: int) -> int:
    return a + b

def subtract(a: int, b: int) -> int:
    return a - b

def factorial(n: int) -> int:
    if n < 0:
        raise ValueError("Liczba nie może być ujemna")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result
