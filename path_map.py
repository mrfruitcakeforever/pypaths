from jsonpath_ng import parse
from functools import partial
from pathlib import Path

def jsonpath_values(source:dict, path:str):
    parser = parse(path)
    matches = parser.find(source)
    if matches:
        return list(map(lambda match:match.value, matches))
    return matches

def path_from_dict(path: Path, source:dict):
    json_path = '.'.join(path.parts)
    return jsonpath_values(source, json_path)

