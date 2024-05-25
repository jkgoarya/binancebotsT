import configparser
import logging

def load_config(general_config_path, secret_config_path):
    config = configparser.ConfigParser()
    try:
        config.read(general_config_path)
        config.read(secret_config_path)  # Augments or overrides with secret settings
        logging.info("Configuration files loaded successfully.")
    except Exception as e:
        logging.error(f"Failed to read configuration files: {e}")
    return config

# Setup basic logging configuration
logging.basicConfig(level=logging.INFO)
