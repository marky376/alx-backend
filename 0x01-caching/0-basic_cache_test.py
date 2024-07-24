class BasicCache:
    """
    BasicCache class with doctests.

    >>> my_cache = BasicCache()
    >>> my_cache.print_cache()
    Current cache:

    >>> my_cache.put("A", "Hello")
    >>> my_cache.put("B", "World")
    >>> my_cache.print_cache()
    Current cache:
    A: Hello
    B: World

    >>> print(my_cache.get("A"))
    Hello

    >>> print(my_cache.get("B"))
    World

    >>> print(my_cache.get("C"))
    None

    >>> my_cache.put("C", "Holberton")
    >>> my_cache.print_cache()
    Current cache:
    A: Hello
    B: World
    C: Holberton

    >>> my_cache.put("D", "School")
    >>> my_cache.put("E", "Battery")
    >>> my_cache.put("A", "Street")
    >>> my_cache.print_cache()
    Current cache:
    B: World
    C: Holberton
    D: School
    E: Battery
    A: Street
    """
    def __init__(self):
        self.cache = {}

    def put(self, key, value):
        """Add a key-value pair to the cache."""
        self.cache[key] = value

    def get(self, key):
        """Retrieve the value for a given key from the cache."""
        return self.cache.get(key)

    def print_cache(self):
        """Print the current cache."""
        print("Current cache:")
        for key, value in self.cache.items():
            print(f"{key}: {value}")

