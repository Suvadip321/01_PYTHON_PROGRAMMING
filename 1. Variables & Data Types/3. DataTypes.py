# --- INTEGER (int) ---
age = 20
print("Age:", age, "| Type:", type(age))
print("Memory Address (id):", id(age))
print("Is age an int?", isinstance(age, int))
# Output:
# Age: 20 | Type: <class 'int'>
# Memory Address (id): <some unique number>
# Is age an int? True


# --- FLOAT (float) ---
pi = 3.14159
print("Pi:", pi, "| Type:", type(pi))
print("Memory Address (id):", id(pi))
print("Is pi a float?", isinstance(pi, float))
# Output:
# Pi: 3.14159 | Type: <class 'float'>
# Memory Address (id): <some unique number>
# Is pi a float? True


# --- STRING (str) ---
language = "Python"
print("Language:", language, "| Type:", type(language))
print("Memory Address (id):", id(language))
print("Is language a str?", isinstance(language, str))
# Output:
# Language: Python | Type: <class 'str'>
# Memory Address (id): <some unique number>
# Is language a str? True


# --- BOOLEAN (bool) ---
is_student = True
print("is_student:", is_student, "| Type:", type(is_student))
print("Memory Address (id):", id(is_student))
print("Is is_student a bool?", isinstance(is_student, bool))
# Output:
# is_student: True | Type: <class 'bool'>
# Memory Address (id): <some unique number>
# Is is_student a bool? True


# --- NONE TYPE (NoneType) ---
data = None
print("data:", data, "| Type:", type(data))
print("Memory Address (id):", id(data))
print("Is data NoneType?", isinstance(data, type(None)))
# Output:
# data: None | Type: <class 'NoneType'>
# Memory Address (id): <some unique number>
# Is data NoneType? True

# --- Complex ---
x = 7j
print("x:", x, "| Type:", type(x))
print("Memory Address (id):", id(x))
print("Is x a complex number?", isinstance(x, complex))
# Output
# x: 7j | Type: <class 'complex'>
# Memory Address (id): <some unique number>
# Is x a complex number? True

