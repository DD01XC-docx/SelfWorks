
# ====== ОСНОВНОЙ КЛАСС УСТРОЙСТВА ======
class Device:
    """
    Базовый класс для всех устройств в умном доме.
    """
    def __init__(self, name, device_type):
        self.name = name
        self.device_type = device_type
        self.is_on = False

    def get_status(self):
        """Возвращает строку с текущим статусом устройства."""
        status = "вкл" if self.is_on else "выкл"
        return f"{self.name} ({self.device_type}): {status}"

    # ЗАДАНИЕ 1: Реализуйте метод can_perform_action.
    # Он должен проверять, может ли устройство выполнить какое-либо действие в принципе.
    # Пока что просто возвращайте True. Этот метод будут переопределять дочерние классы.
    def can_perform_action(self):
        return True

# ====== КЛАСС ЛАМПЫ ======
class Light(Device):
    """
    Класс для представления умной лампы.
    Лампа имеет уровень заряда и может включаться только если заряд выше 10%.
    """
    def __init__(self, name, battery_level=100):
        # ЗАДАНИЕ 2: Инициализируйте класс-родитель (Device) с помощью super().
        # Передайте ему name и device_type="Лампа".
        super().__init__(name, device_type="Лампа")
        self.battery_level = battery_level
        pass

    # ЗАДАНИЕ 3: Переопределите метод get_status, чтобы он также показывал уровень заряда.
    # Например: "Гостиная (Лампа): выкл (Заряд: 50%)"
    def get_status(self):
        status = "вкл" if self.is_on else "выкл"
        return f"{self.name} ({self.device_type}): {status} (Заряд: {self.battery_level}%)"
        pass

    # ЗАДАНИЕ 4: Переопределите метод can_perform_action.
    # Лампа может действовать (включиться/выключиться), только если ее заряд > 10.
    # Верните True, если заряд достаточный, и False - если нет.
    def can_perform_action(self):
        return self.battery_level > 10
        pass
    def turn_on(self):
        """Включает лампу, если это возможно."""
        if self.can_perform_action():
            self.is_on = True
            print(f"{self.name} включена.")
        else:
            print(f"Ошибка: {self.name} не может быть включена. Низкий заряд.")

    def turn_off(self):
        """Выключает лампу."""
        self.is_on = False
        print(f"{self.name} выключена.")

# ====== КЛАСС ТЕРМОСТАТА ======
class Thermostat(Device):
    """
    Класс для представления умного термостата.
    """
    def __init__(self, name, current_temp=20, target_temp=22):
        # ЗАДАНИЕ 5: Инициализируйте класс-родитель (Device). device_type="Термостат".
        self.current_temp = current_temp
        self.target_temp = target_temp
        self.is_on = False # Термостат изначально выключен
        super().__init__(name, device_type="Термостат")
        pass 

    def get_status(self):
        # ЗАДАНИЕ 6: Переопределите метод get_status.
        # Он должен возвращать строку вида: "Гостиная (Термостат): вкл (21°C -> 22°C)"
        status = "вкл" if self.is_on else "выкл"
        return f"{self.name} ({self.device_type}): {status} ({self.current_temp})°C -> {self.target_temp}°C)"
        pass

    # ЗАДАНИЕ 7: Переопределите метод can_perform_action.
    # Термостат может работать всегда (у него нет ограничения по заряду).
    # Просто верните True.
    def can_perform_action(self):
        return True
        pass

    def set_target_temp(self, new_temp):
        """Устанавливает целевую температуру и включает термостат."""
        if self.can_perform_action():
            self.target_temp = new_temp
            self.is_on = True # Термостат включается при установке температуры
            print(f"{self.name} установлена температура {new_temp}°C.")
        else:
            print(f"Ошибка: {self.name} не может выполнить действие.")

# ====== КЛАСС УМНОГО ДОМА ======
class SmartHome:
    """
    Класс, который представляет собой умный дом и управляет устройствами.
    """
    def __init__(self, time_of_day="День"):
        self.devices = []
        self.time_of_day = time_of_day # Может быть "День" или "Вечер"

    def add_device(self, device):
        """Добавляет устройство в умный дом."""
        self.devices.append(device)

    def simulate_evening(self):
        """Симулирует наступление вечера."""
        self.time_of_day = "Вечер"
        print("\n--- Наступил вечер ---")

        # ЗАДАНИЕ 8: Реализуйте логику автоматического включения ламп.
        # Пройдитесь по всем устройствам в self.devices.
        # Если устройство является лампой (проверьте type(device) == Light) И
        # если сейчас "Вечер", то вызовите у лампы метод turn_on().

        for device in self.devices:
            if type(device) == Light and self.time_of_day == "Вечер":
                device.turn_on()
            pass
    def print_status_report(self):
        """Выводит отчет о состоянии всех устройств в доме."""
        print("\n=== Отчет о состоянии умного дома ===")
        print(f"Время суток: {self.time_of_day}")
        for device in self.devices:
            print(f"  - {device.get_status()}")

# ====== ТОЧКА ВХОДА (ОСНОВНАЯ ЛОГИКА ПРОГРАММЫ) ======
if __name__ == "__main__":
    # Создаем умный дом
    my_home = SmartHome()
  
    # Создаем устройства
    kitchen_light = Light("Кухонная лампа", battery_level=50)
    living_room_thermostat = Thermostat("Гостиная термостат", 21, 22)

    # Добавляем устройства в дом
    my_home.add_device(kitchen_light)
    my_home.add_device(living_room_thermostat)

    # Показываем начальный статус
    my_home.print_status_report()

    # Пробуем включить лампу днем (она не должна включиться автоматически)
    print("\n--- Пытаюсь включить лампу днем ---")
    kitchen_light.turn_on()

    # Симулируем наступление вечера (лампы должны включиться автоматически)
    my_home.simulate_evening()

    # Устанавливаем новую температуру на термостате
    print("\n--- Устанавливаю температуру ---")
    living_room_thermostat.set_target_temp(24)

    # Показываем финальный статус
    my_home.print_status_report()