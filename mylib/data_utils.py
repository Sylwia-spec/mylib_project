def flatten_list(nested):
    """Spłaszcza zagnieżdżoną listę."""
    return [item for sublist in nested for item in sublist]
