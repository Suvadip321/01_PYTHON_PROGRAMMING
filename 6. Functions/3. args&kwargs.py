# *ARGS and **KWARGS

# *args (variable positional arguments)
def nums_tuple(*nums):
    """Accepts any number of positional arguments (packed into a tuple)"""
    return nums

print(nums_tuple(1, 2, 3, 4, 5))

# **kwargs (variable keyword arguments)
def info_dict(**info):
    """Accepts any number of keyword arguments (packed into a dict)"""
    return info

print(info_dict(name="Suvadip", age=20, city="Kolkata"))


# Mixing normal args + *args + **kwargs
def model_config(model_name, *layers, **params):
    print("Model:", model_name)
    print("Layers:", layers)
    print("Parameters:", params)

model_config(
                "ANN",
                "Input", "Dense", "Output",
                learning_rate=0.01, epochs=50, optimizer="adam"
            )
