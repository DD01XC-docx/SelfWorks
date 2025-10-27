import functools
from SecurityContext import Context 

def require_role(role):
    """Аспект безопасности — проверяет роль"""
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            current_user = Context.get_current_user() # Получаем текущего пользователя
            if current_user is None:
                raise PermissionError("Нет доступа: пользователь не аутентифицирован")
            if current_user["role"] != role:
                raise PermissionError(f"Нет доступа: требуется роль {role}")
            print(f"[SECURITY] Доступ разрешён пользователю {current_user['name']}")
            return func(*args, **kwargs)
        return wrapper
    return decorator
