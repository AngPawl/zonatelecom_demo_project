import json
import os


def load_schema(name):
    current_dir = os.path.dirname(__file__)
    dir = os.path.dirname(current_dir)
    rootdir = os.path.dirname(dir)

    path = os.path.join(rootdir, dir, 'data', 'json_schemes', name)

    with open(path) as file:
        json_schema = json.loads(file.read())

    return json_schema
