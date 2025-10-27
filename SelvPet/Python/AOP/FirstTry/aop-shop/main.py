from shop.products import get_product_details
# main.py

from shop.products import get_product_details
from shop.orders import delete_order
from SecurityContext import Context # Предположим, это правильный импорт

if __name__ == "__main__":
    # --- НОВЫЙ КОД ДЛЯ ВВОДА ПОЛЬЗОВАТЕЛЯ ---
    current_user_name = input("Введите ваше имя: ")
    current_user_role = input("Введите вашу роль (например, 'user' или 'admin'): ")
    print(Context.set_current_user(current_user_name, current_user_role))
    print("---------------------------------------")
    # ----------------------------------------
    
    # 1. Получаем информацию о товаре (должно работать для всех)
    print("\n[==>] Получаем информацию о товаре [==>]")
    get_product_details(1)
    get_product_details(1) # второй раз - будет кэш

    # 2. Пытаемся удалить заказ (должно упасть, если роль не admin)
    print("\n[==>] Пытаемся удалить заказ [==>]")
    try:
        delete_order(100)
    except PermissionError as e:
        print(f"Ошибка: {e} так как роль не admin")
        
    # 3. Меняем роль на admin и пробуем снова
    print("\n[==>] Меняем роль на admin и пробуем снова [==>]")
    
    # Запрашиваем новую роль для теста
    new_role = input("Введите роль для повторной попытки ('admin' для успеха): ")
    Context.set_current_user(current_user_name, new_role)
    
    delete_order(100)