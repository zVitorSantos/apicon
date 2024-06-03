# from data.sensio_api import get_products
# from data.effecti_api import import_products
# from utils.helpers import transform_product_to_import_format
from data.effecti_api import get_proposals

def main():
    page = 0
    all_proposals = []
    while True:
        proposals, total_records = get_proposals(page)
        if not proposals:
            break
        all_proposals.extend(proposals)
        page += 1
        if len(all_proposals) >= total_records:
            break

    print(f'Total de propostas carregadas: {len(all_proposals)}')
    if all_proposals:
        for i, proposal in enumerate(all_proposals):
            print_proposal(proposal)

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

# def main():
#     products = get_products()
#     if products:
#         proposals = [transform_product_to_import_format(product) for product in products]
#         print(f"Total de propostas geradas: {len(proposals)}")  # Depuração para a quantidade de propostas geradas

#         # Dividindo os produtos em lotes menores
#         batch_size = 50  # Defina o tamanho do lote
#         for i in range(0, len(proposals), batch_size):
#             batch = proposals[i:i+batch_size]
#             try:
#                 import_products(batch)
#             except Exception as e:
#                 print(f'Erro ao importar o lote de produtos: {e}')
#                 # Depuração para identificar quais itens estão falhando
#                 for product in batch:
#                     try:
#                         import_products([product])
#                     except Exception as individual_error:
#                         print(f'Erro ao importar o produto: {product}')
#                         print(f'Erro: {individual_error}')

if __name__ == "__main__":
    main()
