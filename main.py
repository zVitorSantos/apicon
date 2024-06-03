from data.sensio_api import get_products
from data.effecti_api import create_proposal
from utils.helpers import transform_product_to_proposal

def main():
    products = get_products()
    if products:
        # Processando apenas os primeiros 5 produtos para a depuração inicial
        for product in products[:5]:
            print(f"Processando produto: {product}")  # Depuração para cada produto
            proposal = transform_product_to_proposal(product)
            create_proposal(proposal)

if __name__ == "__main__":
    main()
