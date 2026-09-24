def validate_name(name):
    """Return True if name is a string of letters and spaces, at least 2 characters."""
    if not isinstance(name, str):
        return False

    name = name.strip()
    if len(name) < 2:
        return False

    return all(ch.isalpha() or ch.isspace() for ch in name)