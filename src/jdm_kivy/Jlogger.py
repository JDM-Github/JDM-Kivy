
class JDMLogger:
    
    @staticmethod
    def warning(text):
        print(f"JDM LOGGER: [ {'WARNING'.center(20)} ] ---> {text}")
    
    @staticmethod
    def log_config(text):
        print(f"JDM LOGGER: [ {'CONFIG'.center(20)} ] ---> {text}")
    
    @staticmethod
    def log_config_warning(text):
        print(f"JDM LOGGER: [ {'CONFIG WARNING'.center(20)} ] ---> {text}")
    
    @staticmethod
    def log_start_app(text):
        print(f"JDM LOGGER: [ {'JDM APP'.center(20)} ] ---> {text}")
