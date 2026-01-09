import logging

# Logging setup
logging.basicConfig(
    filename="app.log",
    level=logging.ERROR,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# Basic try / except
try:
    value = int("10")
except ValueError:
    pass

# ---------- Multiple except blocks ----------
try:
    result = 10 / 0
except ZeroDivisionError:
    logging.error("Division by zero")
except TypeError:
    logging.error("Invalid type")


# ---------- Catching multiple exceptions ----------
try:
    number = int("abc")
except (ValueError, TypeError):
    logging.error("Invalid conversion")


# ---------- Generic exception (boundary use) ----------
try:
    data = None
    len(data)
except Exception as e:
    logging.error(f"Unexpected error: {e}")


# ---------- else and finally ----------
try:
    x = int("5")
except ValueError:
    logging.error("Conversion failed")
else:
    x = x * 2
finally:
    x = None


# ---------- Raising exceptions ----------
def withdraw(balance, amount):
    if amount > balance:
        raise ValueError("Insufficient balance")
    return balance - amount


# ---------- Custom exception ----------
class ValidationError(Exception):
    pass


def validate_age(age: int):
    if age < 0:
        raise ValidationError("Age must be non-negative")


# ---------- Re-raising exceptions ----------
try:
    int("xyz")
except ValueError:
    logging.error("Re-raising exception")
    raise


# ---------- Handling exceptions in functions ----------
def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return None
