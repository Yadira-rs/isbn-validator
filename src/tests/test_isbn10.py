# tests/test_isbn10.py

import pytest
from src.isbn import is_valid_isbn10

@pytest.mark.parametrize("isbn,esperado", [
    ("0-306-40615-2", True),        # válido
    ("0471958697", True),           # válido sin guiones
    ("0-8044-2957-X", True),        # válido con X final
    ("0-8044-2957-9", False),       # checksum incorrecto
    ("123456789", False),           # longitud 9
    ("12345678901", False),         # longitud 11
    ("0-306-40A15-2", False),       # carácter ilegal
    ("X471958697", False),          # X no al final
])
def test_isbn10_validez(isbn, esperado):
    assert is_valid_isbn10(isbn) == esperado
