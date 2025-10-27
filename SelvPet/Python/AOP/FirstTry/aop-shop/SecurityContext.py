class Context:

    @classmethod
    def set_current_user(cls, name, role):
        cls.current_user = {"name": name, "role": role}

    @classmethod
    def get_current_user(cls):
        return cls.current_user
    
