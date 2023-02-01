from jsonpath_ng import parse
from functools import partial
from pathlib import Path
from toolz import identity, itemmap

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

# {key: functional_value}
# {f1: f2{


