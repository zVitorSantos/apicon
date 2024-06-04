import requests
from config.config import EFFECTI_API_USERNAME, EFFECTI_API_PASSWORD, EFFECTI_API_KEY

def login_and_get_token():
    url = "https://mdw.minha.effecti.com.br/users/login"
    payload = {
        "username": EFFECTI_API_USERNAME,
        "password": EFFECTI_API_PASSWORD
    }
    headers = {
        "Content-Type": "application/json"
    }
    try:
        response = requests.post(url, json=payload, headers=headers)
        response.raise_for_status()
        response_data = response.json()
        token = response_data.get("token")
        return token
    except requests.exceptions.HTTPError as http_err:
        print(f'Erro HTTP: {http_err}')
        print(f'Resposta do servidor: {response.text}')
    except requests.exceptions.RequestException as req_err:
        print(f'Erro ao fazer a requisição: {req_err}')
    except Exception as e:
        print(f'Erro inesperado: {e}')
    return None

def import_products(products_data, token):
    url = "https://mdw.minha.effecti.com.br/produto/salvar"
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }
    successful_imports = 0
    for product in products_data:
        try:
            response = requests.post(url, json=product, headers=headers)
            response.raise_for_status()
            response_data = response.json()
            if response_data.get('success'):
                successful_imports += 1
            else:
                print(f'Falha ao importar produto: {response_data}')
        except requests.exceptions.HTTPError as http_err:
            print(f'Erro HTTP: {http_err}')
            print(f'Resposta do servidor: {response.text}')
        except requests.exceptions.RequestException as req_err:
            print(f'Erro ao fazer a requisição: {req_err}')
        except Exception as e:
            print(f'Erro inesperado: {e}')
    print(f'{successful_imports} produtos importados com sucesso.')

def get_proposals(page, token):
    url = f"https://mdw.minha.effecti.com.br/proposta/minhas"
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }
    payload = {
        "pagina": page,
        "tipo": [],
        "isSrp": False,
        "portal": [],
        "dataEnvioEmail": {},
        "dataInicial": {},
        "dataFinal": {},
        "beginDate": {"equal": "", "less": "", "more": ""},
        "bidding": "",
        "companyName": "",
        "date": {"equal": "", "less": "", "more": ""},
        "deserto": False,
        "endDate": {"equal": "", "less": "", "more": ""},
        "eventStatus": False,
        "favorito": False,
        "interesse": True,
        "isMonitoring": False,
        "isSRP": False,
        "ordem": {"date": "desc"},
        "portalName": [],
        "pregao": "",
        "sendedDate": {"equal": "", "less": "", "more": ""},
        "status": "",
        "uasg": "",
        "uasgName": "",
        "uf": "",
        "user": ""
    }
    try:
        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()
        response_data = response.json()
        proposals = response_data.get('data', {}).get('data', [])
        total_records = response_data.get('data', {}).get('recordsTotal', 0)
        return proposals, total_records
    except requests.exceptions.HTTPError as http_err:
        print(f'Erro HTTP: {http_err}')
        print(f'Resposta do servidor: {response.text}')
    except requests.exceptions.RequestException as req_err:
        print(f'Erro ao fazer a requisição: {req_err}')
    except Exception as e:
        print(f'Erro inesperado: {e}')
    return [], 0
