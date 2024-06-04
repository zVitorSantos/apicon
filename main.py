from data.sensio_api import get_products, get_sales
from data.effecti_api import import_products, login_and_get_token, get_proposals
from utils.helpers import transform_product_to_import_format
from tqdm import tqdm
import json
import os
from datetime import datetime

# Função para carregar a data da última verificação
def load_last_check_date():
    if os.path.exists("config.json"):
        with open("config.json", "r") as file:
            config = json.load(file)
            return config.get("last_check_date")
    return None

# Função para salvar a data da última verificação
def save_last_check_date(date_str):
    config = {"last_check_date": date_str}
    with open("config.json", "w") as file:
        json.dump(config, file)

# Função para carregar IDs de produtos já importados
def load_imported_product_ids():
    if os.path.exists("imported_products.json"):
        with open("imported_products.json", "r") as file:
            return json.load(file)
    return []

# Função para salvar IDs de produtos importados
def save_imported_product_ids(imported_ids):
    with open("imported_products.json", "w") as file:
        json.dump(imported_ids, file)

def print_proposal(proposal):
    print(f"Proposta ID = {proposal.get('id', 'Sem ID')}")
    print(f"Edital ID = {proposal.get('editalId', 'Sem Edital ID')}")
    print(f"Edital URL = {proposal.get('editalUrl', 'Sem Edital URL')}")
    print(f"Portal = {proposal.get('portalName', 'Sem Portal')}")
    print(f"Empresa = {proposal.get('companyName', 'Sem Empresa')}")
    print(f"Licitação = {proposal.get('bidding', 'Sem Licitação')}")
    print(f"UASG = {proposal.get('uasg', 'Sem UASG')}")
    print(f"Nome UASG = {proposal.get('uasgName', 'Sem Nome UASG')}")
    print(f"Status = {proposal.get('status', 'Sem Status')}")
    print(f"SRP = {proposal.get('isSRP', 'Sem SRP')}")
    print(f"Data = {proposal.get('date', 'Sem Data')}")
    print(f"Data de Envio = {proposal.get('sendedDate', 'Sem Data de Envio')}")
    print(f"Data de Início = {proposal.get('beginDate', 'Sem Data de Início')}")
    print(f"Data de Término = {proposal.get('endDate', 'Sem Data de Término')}")
    print(f"Status do Evento = {proposal.get('eventStatus', 'Sem Status do Evento')}")
    print(f"Monitoramento = {proposal.get('isMonitoring', 'Sem Monitoramento')}")
    print(f"Mensagem = {proposal.get('message', 'Sem Mensagem')}")
    print(f"Portal ID = {proposal.get('portalId', 'Sem Portal ID')}")
    print(f"Filial = {proposal.get('branch', 'Sem Filial')}")
    print(f"Modalidade = {proposal.get('modality', 'Sem Modalidade')}")
    print(f"Usuário = {proposal.get('user', 'Sem Usuário')}")
    print(f"Cidade = {proposal.get('city', 'Sem Cidade')}")
    print("-" * 80)

def print_sales(sales):
    for sale in sales:
        print(f"ID do Pedido: {sale.get('_id', 'Sem ID')}")
        print(f"Código: {sale.get('code', 'Sem Código')}")
        print(f"Data de Criação: {sale.get('dateCreated', 'Sem Data')}")
        print(f"ID do Cliente: {sale.get('customerId', 'Sem ID do Cliente')}")
        print(f"Nome do Cliente: {sale.get('personName', 'Sem Nome')}")
        print(f"Tipo: {sale.get('type', 'Sem Tipo')}")
        print(f"Status: {sale.get('status', 'Sem Status')}")
        print(f"PO: {sale.get('po', 'Sem PO')}")
        print(f"NFE: {sale.get('nfe', 'Sem NFE')}")
        print(f"Status da NFE: {sale.get('nfeStatus', 'Sem Status da NFE')}")
        print("-" * 80)

def main():
    token = login_and_get_token()
    if not token:
        print("Erro ao obter o token de autenticação.")
        return

    imported_product_ids = load_imported_product_ids()
    last_check_date = load_last_check_date()

    products = get_products()
    if products:
        proposals = []
        for product in products:
            product_id = product.get('_id')
            if product_id not in imported_product_ids:
                proposals.append(transform_product_to_import_format(product))
                imported_product_ids.append(product_id)
        
        if not proposals:
            print("Nenhum novo produto para importar.")
        else:
            print(f"Total de propostas geradas: {len(proposals)}")  # Depuração para a quantidade de propostas geradas

            # Importando os produtos individualmente com barra de progresso
            try:
                for product in tqdm(proposals, desc="Importando produtos"):
                    import_products([product], token)
                save_imported_product_ids(imported_product_ids)
            except Exception as e:
                print(f'Erro ao importar produtos: {e}')
    
    # Coletar as propostas
    page = 0
    all_proposals = []
    while True:
        proposals, total_records = get_proposals(page, token)
        if not proposals:
            break
        all_proposals.extend(proposals)
        page += 1
        if len(all_proposals) >= total_records:
            break

    print(f'Total de propostas carregadas: {len(all_proposals)}')

    # Filtrar propostas novas baseadas na data da última verificação
    new_proposals = []
    if last_check_date:
        last_check_datetime = datetime.strptime(last_check_date, '%d/%m/%Y %H:%M:%S')
        new_proposals = [proposal for proposal in all_proposals if datetime.strptime(proposal['date'], '%d/%m/%Y %H:%M:%S') > last_check_datetime]
    else:
        new_proposals = all_proposals

    if new_proposals:
        for i, proposal in enumerate(new_proposals):
            # print_proposal(proposal)
            print(i+1)
    else:
        print("Nenhuma nova proposta encontrada desde a última verificação.")
    
    # Atualizar a data da última verificação
    current_time_str = datetime.now().strftime('%d/%m/%Y %H:%M:%S')
    save_last_check_date(current_time_str)
    
    # Coletar os pedidos do Sensio
    sales_page = 1
    while True:
        sales = get_sales(sales_page)
        if not sales:
            break
        #print_sales(sales)
        sales_page += 1

if __name__ == "__main__":
    main()
