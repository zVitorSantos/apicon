import requests
from config.config import SENSIO_BASE_URL, SENSIO_API_KEY

def get_sales(page, status=None, search=None):
    url = f"{SENSIO_BASE_URL}/sales/list/{page}"
    headers = {
        "Authorization": f"Bearer {SENSIO_API_KEY}",
        "Content-Type": "application/json"
    }
    params = {}
    if status:
        params['status'] = status
    if search:
        params['search'] = search

    try:
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()
        response_data = response.json()
        sales = response_data.get('response', [])
        return sales
    except requests.exceptions.HTTPError as http_err:
        print(f'Erro HTTP: {http_err}')
        print(f'Resposta do servidor: {response.text}')
    except requests.exceptions.RequestException as req_err:
        print(f'Erro ao fazer a requisição: {req_err}')
    except Exception as e:
        print(f'Erro inesperado: {e}')
    return []

def get_products():
    url = f"{SENSIO_BASE_URL}/items"
    headers = {
        "Authorization": f"bearer {SENSIO_API_KEY}",
        "Content-Type": "application/json"
    }
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        response_data = response.json()
        items = response_data.get('response', {}).get('items', [])
        # Verificar se a resposta contém itens
        if items:
            print(f'Total de itens carregados: {len(items)}')
            return items
        else:
            print(f'Estrutura inesperada na resposta da API: {response_data}')
            return None
    except requests.exceptions.HTTPError as http_err:
        print(f'Erro HTTP: {http_err}')
        print(f'Resposta do servidor: {response.text}')
    except requests.exceptions.RequestException as e:
        print(f'Erro ao obter itens do Sensio: {e}')
    return None
