import yaml

def load_config(config_path: str, key: str = None):
    with open(config_path, "r") as file:
        config = yaml.safe_load(file)
        if key is not None:
            try:
                return config.get(key)
            except KeyError:
                raise KeyError(f"Key '{key}' not found in config file.")
        return config
