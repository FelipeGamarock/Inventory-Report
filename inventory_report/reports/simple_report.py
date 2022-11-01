from statistics import mode


class SimpleReport:
    def __init__(self):
        pass

    @classmethod
    def generate(self, report_infos):
        oldest_date = min(
            [product['data_de_fabricacao'] for product in report_infos]
        )
        closest_date = max(
            [product['data_de_validade'] for product in report_infos]
        )
        company = mode(
            [product['nome_da_empresa'] for product in report_infos]
        )

        return(
            f"Data de fabricação mais antiga: {oldest_date}\n"
            f"Data de validade mais próxima: {closest_date}\n"
            f"Empresa com mais produtos: {company}"
        )
