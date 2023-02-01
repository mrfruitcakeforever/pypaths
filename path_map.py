from jsonpath_ng import parse
from functools import partial

def jsonpath_values(source:dict, path:str):
    parser = parse(path)
    matches = parser.find(source)
    if matches:
        return list(map(lambda match:match.value, matches))
    return matches

