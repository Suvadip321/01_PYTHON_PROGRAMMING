class Vector:
    def __init__(self, x, y):      # __init__: object constructor
        self.x = x
        self.y = y

    def __repr__(self):            # __repr__: unambiguous representation
        return f"Vector({self.x}, {self.y})"

    def __str__(self):             # __str__: user-friendly string
        return f"({self.x}, {self.y})"

    def __len__(self):             # __len__: length (used with len())
        return 2

    def __getitem__(self, index):  # __getitem__: indexing support
        return (self.x, self.y)[index]

    def __iter__(self):            # __iter__: makes object iterable
        return iter((self.x, self.y))

    def __eq__(self, other):       # __eq__: equality check
        return (self.x, self.y) == (other.x, other.y)

    def __add__(self, other):      # __add__: + operator
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):      # __sub__: - operator
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, scalar):     # __mul__: * operator
        return Vector(self.x * scalar, self.y * scalar)

    def __call__(self):            # __call__: make object callable
        return f"Vector at ({self.x}, {self.y})"

v1 = Vector(2, 3)
v2 = Vector(4, 1)

print("repr:", repr(v1))         # Vector(2, 3)
print("str:", str(v1))           # (2, 3)
print("len:", len(v1))           # 2
print("indexing:", v1[0], v1[1]) # 2 3
print("iter:", list(v1))         # [2, 3]
print("equality:", v1 == Vector(2, 3))  # True
print("addition:", v1 + v2)      # (6, 4)
print("subtraction:", v1 - v2)   # (-2, 2)
print("multiplication:", v1 * 3) # (6, 9)
print("call:", v1())             # Vector at (2, 3)
