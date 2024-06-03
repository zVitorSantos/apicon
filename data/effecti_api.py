import requests
from config.config import EFFECTI_BASE_URL, EFFECTI_API_KEY

def import_products(products_data):
    url = f"https://mdw.minha.effecti.com.br/proposta/minhas"
    headers = {
        "Authorization": f"Bearer {EFFECTI_API_KEY}",
        "Content-Type": "application/json"
    }
    try:
        response = requests.post(url, json=products_data, headers=headers)
        response.raise_for_status()
        print(f'{len(products_data)} produtos importados com sucesso.')
    except requests.exceptions.HTTPError as http_err:
        print(f'Erro HTTP: {http_err}')
        print(f'Resposta do servidor: {response.text}')
        raise 
    except requests.exceptions.RequestException as req_err:
        print(f'Erro ao fazer a requisição: {req_err}')
        raise  
    except Exception as e:
        print(f'Erro inesperado: {e}')
        raise 

def get_proposals(page):
    url = "https://mdw.minha.effecti.com.br/proposta/minhas"
    headers = {
        "Authorization": f"Bearer {EFFECTI_API_KEY}",
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
        # print(f'Request URL: {url}')
        # print(f'Headers: {headers}')
        # print(f'Payload: {payload}')
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