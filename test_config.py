from configparser import ConfigParser

def test_config():
    config = ConfigParser()
    config.read(['config.ini', 'secret.cfg'])
    print("Sections found:", config.sections())

test_config()
