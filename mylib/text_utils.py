def count_words(text: str) -> int:
    """
    Zlicza liczbę słów w podanym tekście.
    """
    return len(text.strip().split())


def reverse_text(text: str) -> str:
    """Zwraca odwrócony tekst."""
    return text[::-1]
