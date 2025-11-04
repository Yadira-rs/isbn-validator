# tests/test_properties.py

from src.isbn import normalize_isbn, detect_isbn

def test_normalize_idempotente():
    """Verifica que normalizar dos veces produce el mismo resultado."""
    s = "978-0-306-40615-7"
    assert normalize_isbn(normalize_isbn(s)) == normalize_isbn(s)

def test_normalize_elimina_espacios_y_guiones():
    """Verifica que se eliminen guiones y espacios correctamente."""
    assert normalize_isbn("978 0 306 40615 7") == "9780306406157"

def test_detect_isbn_formats():
    """Prueba la detección de formato correcto."""
    assert detect_isbn("0-8044-2957-X") == "ISBN-10"
    assert detect_isbn("9780306406157") == "ISBN-13"
    assert detect_isbn("9780306406158") == "INVALID"

def test_detect_vacio():
    """Verifica que una cadena vacía sea inválida."""
    assert detect_isbn("") == "INVALID"
