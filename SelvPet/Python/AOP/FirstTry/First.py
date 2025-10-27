
# -----------Aspect Definition-------------------------------------------
import functools

def log_aspect(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Calling function: {func.__name__}")
        result = func(*args, **kwargs)
        print(f"Function {func.__name__} returned: {result}")
        return result
    return wrapper
def time_aspect(func):
    import time
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Function {func.__name__} took {end_time - start_time:.4f} seconds")
        return result
# --------------------------------------------------------------
# -----------Business Logic-------------------------------------------
@time_aspect
@log_aspect
def save_user(name):
    print(f"Saving user: {name}")
    return True

@time_aspect
@log_aspect
def delete_user(user_id):
    print(f"Deleting user with ID: {user_id}")
    return "OK"

# --------------------------------------------------------------
# -----------Main Application-------------------------------------------
if __name__ == "__main__":
    save_user("Alice")
    delete_user(42)
# --------------------------------------------------------------