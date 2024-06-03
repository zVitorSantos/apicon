import requests
from config.config import SENSIO_BASE_URL, SENSIO_API_KEY
from utils.helpers import print_limited_items

def get_products():
    url = f"{SENSIO_BASE_URL}/items"
    headers = {
        "Authorization": f"bearer {SENSIO_API_KEY}",
        "Content-Type": "application/json"
    }
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        items = response.json()
        # Verificar se a resposta é uma lista
        if isinstance(items, list):
            print(f'Total de itens carregados: {len(items)}')
            print_limited_items(items)
            return items
        else:
            print(f'Estrutura inesperada na resposta da API: {items}')
            return None
    except requests.exceptions.HTTPError as http_err:
        print(f'Erro HTTP: {http_err}')
        print(f'Resposta do servidor: {response.text}')
    except requests.exceptions.RequestException as e:
        print(f'Erro ao obter itens do Sensio: {e}')
    return None
