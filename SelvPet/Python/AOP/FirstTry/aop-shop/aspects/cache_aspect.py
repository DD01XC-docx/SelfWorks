import functools

def cache_aspect(func):
    """Аспект кэширования"""
    cache = {}
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        key = (args, tuple(sorted(kwargs.items())))
        if key in cache:
            print(f"[CACHE] Используем кэш для {func.__name__} с {args}")
            return cache[key]
        result = func(*args, **kwargs)
        cache[key] = result
        print(f"[CACHE] Результат сохранён в кэш для {func.__name__}")
        return result
    return wrapper
