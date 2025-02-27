# gets contacted for data by controller
# reads json table
# returns data

import json

def get_data():
    json_file_path = 'ExternalJson/editor_extension.json'

    with open(json_file_path, 'r') as f:
        return json.load(f)

