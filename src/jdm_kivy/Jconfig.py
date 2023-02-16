import os
import json

class JDMConfig:

    @staticmethod
    def _change_Config(name, value):
        first, _ =  os.path.split(__file__)
        with open(f"{first}/config.json") as f:
            config = json.load(f)
        config[name] = value
        with open(f"{first}/config.json", "w") as f:
            json.dump(config, f, indent=2)
    
    @staticmethod
    def reset(name: str): JDMConfig._change_Config(name, 0)
    @staticmethod
    def set(name: str, value: any): JDMConfig._change_Config(name, value)
    @staticmethod
    def activate_root_clock(): JDMConfig._change_Config("root_clock", True)
    @staticmethod
    def deactivate_root_clock(): JDMConfig._change_Config("root_clock", False)
