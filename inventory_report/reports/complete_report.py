from typing import Counter
from simple_report import SimpleReport


class CompleteReport(SimpleReport):
    def __init__(self):
        pass

    @classmethod
    def generate(cls, report_infos):
        simple_report = super().generate(report_infos)

        company_quantities = Counter(
            product["nome_da_empresa"] for product in report_infos
        )
        print(company_quantities)
        company_report = ""
        for company in company_quantities:
            company_report += f"{company}: {company_quantities[company]}\n"
        print(company_report)
        return (
            f"{simple_report}\n"
            f"Produtos estocados por empresa:\n"
            f"{company_report}"
        )


# CompleteReport.generate(
#     [
#         {
#             "id": 1,
#             "nome_do_produto": "MESA",
#             "nome_da_empresa": "Forces of Nature",
#             "data_de_fabricacao": "2022-05-04",
#             "data_de_validade": "2023-02-09",
#             "numero_de_serie": "FR48",
#             "instrucoes_de_armazenamento": "Conservar ao abrigo de luz",
#         },
#         {
#             "id": 2,
#             "nome_do_produto": "MESA",
#             "nome_da_empresa": "Forces of Nature",
#             "data_de_fabricacao": "2022-05-04",
#             "data_de_validade": "2023-02-09",
#             "numero_de_serie": "FR48",
#             "instrucoes_de_armazenamento": "Conservar ao abrigo de luz",
#         },
#         {
#             "id": 3,
#             "nome_do_produto": "MESA",
#             "nome_da_empresa": "Infinity Edge",
#             "data_de_fabricacao": "2022-05-04",
#             "data_de_validade": "2023-02-09",
#             "numero_de_serie": "FR48",
#             "instrucoes_de_armazenamento": "Conservar ao abrigo de luz",
#         },
#     ]
# )
