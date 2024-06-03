from bs4 import BeautifulSoup

def clean_html(raw_html):
    if raw_html is None:
        raw_html = ""
    soup = BeautifulSoup(raw_html, "html.parser")
    cleaned_text = soup.get_text()
    cleaned_text = cleaned_text.replace("🌟", "")
    return cleaned_text

def get_latest_price(product):
    price_history = product.get('priceCostHistory', [])
    latest_price = 0
    if price_history:
        sorted_price_history = sorted(price_history, key=lambda x: x.get('changeDate', ''), reverse=True)
        latest_price = sorted_price_history[0].get('newValue', 0)
    return latest_price

def transform_product_to_import_format(product):
    cleaned_description = clean_html(product.get('description', ''))
    if not cleaned_description:
        cleaned_description = "Sem descrição."
    return {
        "classe": 0,
        "segmento": product.get('segmento', ''),
        "gtnean": product.get('ean', ''),
        "ncm": product.get('ncm', ''),
        "descricao": cleaned_description,
        "observacoes": product.get('observacoes', ''),
        "tipo": 1,
        "referencia": product.get('reference', ''),
        "origem": product.get('origem', 'BR'),  # Definindo "BR" como valor padrão
        "marca": product.get('brand', ''),
        "modelo": product.get('modelo', ''),
        "fornecedor": product.get('fornecedor', ''),
        "tipoMedicamente": 0,
        "registerAnvisa": product.get('registerAnvisa', ''),
        "ppb": product.get('ppb', False),
        "altura": product.get('height', 0) if product.get('height') is not None else 0,
        "largura": product.get('width', 0) if product.get('width') is not None else 0,
        "comprimento": product.get('itemLength', 0) if product.get('itemLength') is not None else 0,
        "peso": product.get('grossWeight', 0) if product.get('grossWeight') is not None else 0,
        "unidade": product.get('dimension', ''),
        "custo": get_latest_price(product),  # Usando o valor mais recente como custo
        "valorProposta": 1,  # Valor da proposta definido como 1 por padrão
        "valorLimite": 0
    }
