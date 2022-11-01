from statistics import mode


class SimpleReport:
    def __init__(self):
        pass

    @classmethod
    def generate(cls, report_infos):
        oldest_date = min(
            [product["data_de_fabricacao"] for product in report_infos]
        )

        closest_expiration_date = "2100-01-01"
        for product in report_infos:
            if product["data_de_validade"] < closest_expiration_date:
                closest_expiration_date = product["data_de_validade"]

        company = mode(
            [product["nome_da_empresa"] for product in report_infos]
        )

        return (
            f"Data de fabricação mais antiga: {oldest_date}\n"
            f"Data de validade mais próxima: {closest_expiration_date}\n"
            f"Empresa com mais produtos: {company}"
        )
