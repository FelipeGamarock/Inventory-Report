from inventory_report.reports.simple_report import SimpleReport
from typing import Counter


class CompleteReport(SimpleReport):

    @classmethod
    def generate(cls, report_infos):
        simple_report = super().generate(report_infos)

        company_quantities = Counter(
            product["nome_da_empresa"] for product in report_infos
        )
        company_report = ""
        for company in company_quantities:
            company_report += f"- {company}: {company_quantities[company]}\n"
        return (
            f"{simple_report}\n"
            f"Produtos estocados por empresa:\n"
            f"{company_report}"
        )
