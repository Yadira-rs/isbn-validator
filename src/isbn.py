# src/isbn.py

def normalize_isbn(s: str) -> str:
    """
    Elimina espacios y guiones; valida que sólo queden dígitos o 'X' final (para ISBN-10).
    """
    if not s or not isinstance(s, str):
        return ""
    s = s.replace("-", "").replace(" ", "").upper()
    # Solo se permiten dígitos o 'X'
    if all(c.isdigit() or c == "X" for c in s):
        return s
    return ""


def is_valid_isbn10(s: str) -> bool:
    """
    Valida ISBN-10 según la regla de pesos 10..1:
    (d1×10 + d2×9 + ... + d10×1) % 11 == 0
    """
    s = normalize_isbn(s)
    if len(s) != 10:
        return False

    total = 0
    for i, char in enumerate(s):
        if char == "X":
            if i != 9:  # 'X' sólo puede estar al final
                return False
            num = 10
        elif char.isdigit():
            num = int(char)
        else:
            return False
        total += num * (10 - i)
    return total % 11 == 0


def is_valid_isbn13(s: str) -> bool:
    """
    Valida ISBN-13 según pesos alternos 1 y 3:
    (d1×1 + d2×3 + d3×1 + ... + d13×3) % 10 == 0
    """
    s = normalize_isbn(s)
    if len(s) != 13 or not s.isdigit():
        return False

    total = sum(int(c) * (1 if i % 2 == 0 else 3) for i, c in enumerate(s))
    return total % 10 == 0


def detect_isbn(s: str) -> str:
    """
    Determina si una cadena es ISBN-10, ISBN-13 o inválida.
    """
    s = normalize_isbn(s)
    if is_valid_isbn10(s):
        return "ISBN-10"
    elif is_valid_isbn13(s):
        return "ISBN-13"
    else:
        return "INVALID"
