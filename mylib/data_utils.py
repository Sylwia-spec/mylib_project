def filter_even(numbers: list[int]) -> list[int]:
    return [num for num in numbers if num % 2 == 0]

def average_list(numbers: list[float]) -> float:
    if not numbers:
        raise ValueError("Lista nie może być pusta")
    return sum(numbers) / len(numbers)

def count_words(text: str) -> int:
    return len(text.split())
