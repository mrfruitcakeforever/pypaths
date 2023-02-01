from jsonpath_ng import parse
from functools import partial
from pathlib import Path
from toolz import identity, keymap, valmap, flip


def jsonpath_values(source:dict, path:str):
    parser = parse(path)
    matches = parser.find(source)
    if matches:
        return list(map(lambda match:match.value, matches))
    return matches

def path_from_dict(path: Path, source:dict):
    json_path = '.'.join(path.parts)
    return jsonpath_values(source, json_path)

def as_callable(element):
    return partial(identity, element)

def multi_function_hash_map(source: dict):
    ''' key function is source and value is parser'''
    return [item(key()) for key,item in source.items()]

def key_as_callable(source:dict):
    return keymap(as_callable, source)

def path_map(path_map: dict, source:dict):
    return valmap(lambda val: val(source), path_map)

def element(path: str):
    return partial(flip(jsonpath_values), path)
