class Device:
    """
    Base class for all devices in the smart home.
    """
    def __init__(self, name, device_type):
        self.name = name
        self.device_type = device_type
        self.is_on = False

    def get_status(self):
        """Returns a string showing the current device status."""
        status = "on" if self.is_on else "off"
        return f"{self.name} ({self.device_type}): {status}"

    #TASK1: Implement can_perform_action.
    # For now return True. Child classes will override it.
    def can_perform_action(self):
        return True

class Light(Device):
    """
    Class representing a smart light.
    The light has a battery level and can turn on only if the battery is above 10%.
    """
    def __init__(self, name, battery_level=100):
        # TASK 2: Initialize the parent class using super().
        super().__init__(name, device_type="Light")
        self.battery_level = battery_level
        pass

    # TASK 3: Override get_status to also show battery level.
    def get_status(self):
        status = "on" if self.is_on else "off"
        return f"{self.name} ({self.device_type}): {status} (Battery: {self.battery_level}%)"
        pass

    #TASK 4: Override can_perform_action.
    #The light can act only if battery > 10.
    def can_perform_action(self):
        return self.battery_level > 10
        pass

    def turn_on(self):
        """Turns on the light if possible."""
        if self.can_perform_action():
            self.is_on = True
            print(f"{self.name} is now ON.")
        else:
            print(f"Error: {self.name} cannot be turned on. Battery too low.")

    def turn_off(self):
        """Turns off the light."""
        self.is_on = False
        print(f"{self.name} is now OFF.")

class Thermostat(Device):
    """
    Class representing a smart thermostat.
    """
    def __init__(self, name, current_temp=20, target_temp=22):
        # TASK 5: Initialize the parent class. device_type="Thermostat".
        self.current_temp = current_temp
        self.target_temp = target_temp
        self.is_on = False  # Thermostat starts turned off
        super().__init__(name, device_type="Thermostat")
        pass 

    def get_status(self):
        # TASK 6: Override get_status.
        status = "on" if self.is_on else "off"
        return f"{self.name} ({self.device_type}): {status} ({self.current_temp}°C -> {self.target_temp}°C)"
        pass

    # TASK 7: Thermostat can always work, so return True.
    def can_perform_action(self):
        return True
        pass

    def set_target_temp(self, new_temp):
        """Sets the target temperature and turns on the thermostat."""
        if self.can_perform_action():
            self.target_temp = new_temp
            self.is_on = True
            print(f"{self.name} target temperature set to {new_temp}°C.")
        else:
            print(f"Error: {self.name} cannot perform this action.")

class SmartHome:
    """
    Class representing a smart home managing all devices.
    """
    def __init__(self, time_of_day="Day"):
        self.devices = []
        self.time_of_day = time_of_day  # Can be "Day" or "Evening"

    def add_device(self, device):
        """Adds a device to the smart home."""
        self.devices.append(device)

    def simulate_evening(self):
        """Simulates evening arrival."""
        self.time_of_day = "Evening"
        print("\n--- Evening has arrived ---")

        # TASK 8: Automatically turn on lights in the evening.
        for device in self.devices:
            if type(device) == Light and self.time_of_day == "Evening":
                device.turn_on()
            pass

    def print_status_report(self):
        """Prints the status report of all home devices."""
        print("\n=== Smart Home Status Report ===")
        print(f"Time of day: {self.time_of_day}")
        for device in self.devices:
            print(f"  - {device.get_status()}")

if __name__ == "__main__":
    # Create smart home
    my_home = SmartHome()
  
    # Create devices
    kitchen_light = Light("Kitchen Light", battery_level=50)
    living_room_thermostat = Thermostat("Living Room Thermostat", 21, 22)

    # Add devices to smart home
    my_home.add_device(kitchen_light)
    my_home.add_device(living_room_thermostat)

    # Print initial status
    my_home.print_status_report()

    # Try turning on the light during the day (should not turn on automatically)
    print("\n--- Trying to turn on the light during the day ---")
    kitchen_light.turn_on()

    # Simulate evening (lights should turn on automatically)
    my_home.simulate_evening()

    # Set new temperature on thermostat
    print("\n--- Setting thermostat temperature ---")
    living_room_thermostat.set_target_temp(24)

    # Print final status
    my_home.print_status_report()
 