def get_latest_price(product):
    price_history = product.get('priceCostHistory', [])
    latest_price = 0
    if price_history:
        sorted_price_history = sorted(price_history, key=lambda x: x.get('changeDate', ''), reverse=True)
        latest_price = sorted_price_history[0].get('newValue', 0)
    return latest_price

def transform_product_to_import_format(product):
    return {
        "description": product.get('name', 'Sem descrição.'),
        "ppb": product.get('ppb', None),
        "type": 1,
        "medOrTec": product.get('tipoMedicamente', False),
        "origin": product.get('origem', None),
        "reference": product.get('reference', ''),
        "height": product.get('height', 0) if product.get('height') is not None else 0,
        "length": product.get('itemLength', 0) if product.get('itemLength') is not None else 0,
        "weight": product.get('grossWeight', 0) if product.get('grossWeight') is not None else 0,
        "width": product.get('width', 0) if product.get('width') is not None else 0,
        "unity": product.get('dimension', 'a'),
        "cost": get_latest_price(product),
        "value": 0.0001,
        "minValue": 0
    }
