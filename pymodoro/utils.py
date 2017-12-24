class memoize(dict):

    def __init__(self, func):
        self.func = func

    def __call__(self, *args):
        return self[args]

    def __missing__(self, key):
        result = self[key] = self.func(*key)
        return result


# def instantiate(*args, **kwargs):
#     """
#     Use it as a class decorator to create instance of the class.
#     Arguments of decorator are passed to class' `__init__` method.

#     >>> @instantiate(greeting='Hello!')
#     ... class A:
#     ...     def __init__(self, *args, **kwargs):
#     ...         print(kwargs['greeting'])
#     Hello!
#     """

#     def wrapper(class_):
#         return class_(*args, **kwargs)

#     return wrapper
