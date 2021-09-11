import json
from pathlib import Path
from os import getenv

json_data_file = Path('config.json')
# checking if config exists
if json_data_file.resolve().exists():
    data = json.load(json_data_file)

# else load environment variables
else:
    env_vars = [ 'ENDPOINT', 'CERTPATH', 'APIKEY' ]
    data = {}
    for env_var in env_vars:
        data[env_var.lower()] = getenv(env_vars)
