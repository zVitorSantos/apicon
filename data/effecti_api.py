import requests
from config.config import EFFECTI_BASE_URL, EFFECTI_API_KEY

def create_proposal(proposal_data):
    url = f"{EFFECTI_BASE_URL}/produto/salvar"
    headers = {
        "Authorization": f"Bearer {EFFECTI_API_KEY}",
        "Content-Type": "application/json"
    }
    try:
        response = requests.post(url, json=proposal_data, headers=headers)
        response.raise_for_status()
        print(f'Item {proposal_data["description"]} salvo com sucesso.')
    except requests.exceptions.RequestException as e:
        print(f'Erro ao salvar o item {proposal_data["description"]}: {e}')
