# =======================================
# *args and **kwargs
# =======================================

# ----- *args (variable positional arguments) -----
def add_numbers(*args):
    """Accepts any number of positional arguments (packed into a tuple)"""
    print("Args received:", args)  # tuple
    return sum(args)

print("Sum:", add_numbers(1, 2, 3, 4))  # 10


# ----- **kwargs (variable keyword arguments) -----
def print_info(**kwargs):
    """Accepts any number of keyword arguments (packed into a dict)"""
    print("Kwargs received:", kwargs)  # dictionary
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name="Alice", age=25, field="ML")


# ----- Mixing normal args + *args + **kwargs -----
def model_config(model_name, *layers, **params):
    """Example: configuring an ML model"""
    print(f"\nModel: {model_name}")
    print("Layers:", layers)        # tuple of positional arguments
    print("Parameters:", params)    # dictionary of keyword arguments

model_config("NeuralNet", "Input", "Dense", "Output",
            learning_rate=0.01, epochs=50, optimizer="adam")


# ----- Unpacking with * and ** -----
nums = [10, 20, 30]
options = {"learning_rate": 0.05, "epochs": 100}

print("\nUnpacking examples:")
print(add_numbers(*nums))  # same as add_numbers(10, 20, 30)
print_info(**options)      # same as print_info(learning_rate=0.05, epochs=100)
