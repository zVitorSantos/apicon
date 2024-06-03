def transform_product_to_proposal(product):
    return {
        'cost': product.get('cost', 0),
        'description': product.get('description', ''),
        'genre': product.get('genero', ''),
        'gtinean': product.get('ean', ''),
        'height': product.get('height', 0),
        'length': product.get('itemLength', 0),
        'medOrTec': False,
        'minValue': 0,
        'ncm': product.get('ncm', ''),
        'observation': '',
        'origin': None,
        'ppb': None,
        'reference': '',
        'type': 1,
        'unity': product.get('dimension', ''),
        'value': product.get('price', 0),
        'weight': product.get('grossWeight', 0),
        'width': product.get('width', 0),
    }

def print_limited_items(items, limit=5):
    for i, item in enumerate(items[:limit]):
        print(f"Item {i+1}: {item}")
