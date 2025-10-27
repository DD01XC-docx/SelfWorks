from aspects.log_aspect import log_aspect
from aspects.time_aspect import time_aspect
from aspects.cache_aspect import cache_aspect
import time

@log_aspect
@time_aspect
@cache_aspect
def get_product_details(product_id):
    """Имитация запроса к БД"""
    print(f"Загружаю информацию о товаре id={product_id}...")
    time.sleep(1)  # имитация долгого запроса
    return {"id": product_id, "name": "Ноутбук", "price": 999.99}
