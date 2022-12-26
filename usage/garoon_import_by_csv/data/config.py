import os
import yaml

config_file = open(os.path.dirname(__file__) + '/../../config.yml', 'r')
config_data = yaml.safe_load(config_file)
