def is_palindrome(text):
    """Sprawdza, czy tekst jest palindromem ignorując znaki specjalne, spacje i wielkość liter."""
    cleaned = ''.join(char.lower() for char in text if char.isalnum())
    return cleaned == cleaned[::-1]



