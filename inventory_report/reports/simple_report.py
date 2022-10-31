from statistics import mode


def oldest_fabrication_date(products_list):
    oldest_date = min(
        [product['data_de_fabricacao'] for product in products_list]
        )
    return oldest_date


def closest_expiration_date(products_list):
    closest_date = max(
        [product['data_de_validade'] for product in products_list]
        )
    return closest_date


def company_with_more_products(products_list):
    company = mode([product['nome_da_empresa'] for product in products_list])
    return company


class SimpleReport:
    def __init__(self):
        pass

    @classmethod
    def generate(self, report_infos):
        oldest_date = oldest_fabrication_date(report_infos)
        closest_date = closest_expiration_date(report_infos)
        company = company_with_more_products(report_infos)

        return(
            f"Data de fabricação mais antiga: {oldest_date}\n"
            f"Data de validade mais próxima: {closest_date}\n"
            f"Empresa com mais produtos: {company}"
        )
