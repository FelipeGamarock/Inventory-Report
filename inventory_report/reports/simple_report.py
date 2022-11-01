from statistics import mode


class SimpleReport:
    def __init__(self):
        pass

    @classmethod
    def generate(self, report_infos):
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


# print(SimpleReport.generate([
#      {
#        "id": 1,
#        "nome_do_produto": "CADEIRA",
#        "nome_da_empresa": "Forces of Nature",
#        "data_de_fabricacao": "2022-04-04",
#        "data_de_validade": "2023-02-09",
#        "numero_de_serie": "FR48",
#        "instrucoes_de_armazenamento": "Conservar em local fresco"
#      }
#    ]))
