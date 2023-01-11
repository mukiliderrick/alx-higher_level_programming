#! python3

def class_to_json(obj):
    d = {}
    for attr, value in vars(obj).items():
        if isinstance(value(list, dict, str, int, float, bool)):
            d[attr] = value
    return d