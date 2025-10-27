from aspects.log_aspect import log_aspect
from aspects.security_aspect import require_role

@log_aspect
@require_role("admin")
def delete_order(order_id):
    """Удаление заказа — доступно только админу"""
    print(f"Удаляю заказ {order_id}...")
    return f"Заказ {order_id} удалён"
