from config_loader import load_config
from starlight_strategy import StarlightStrategy
import logging

def setup_logging(config):
    logging.basicConfig(level=getattr(logging, config['LOGGING']['level'].upper()), 
                        filename=config['LOGGING']['file'], 
                        format='%(asctime)s - %(levelname)s - %(message)s')

def main():
    config = load_config()
    setup_logging(config)
    strategy = StarlightStrategy(config)
    strategy.scout()

if __name__ == "__main__":
    main()
