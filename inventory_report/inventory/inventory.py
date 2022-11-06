import csv
import json
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


def read_csv_file(path):
    with open(path, encoding="utf-8") as file:
        product_reader = csv.DictReader(file)
        product_list = [product for product in product_reader]
        return product_list


def read_json_file(path):
    with open(path) as file:
        product_list = json.load(file)
        return product_list


class Inventory:

    @classmethod
    def import_data(cls, path, type):
        if "csv" in path:
            product_report = read_csv_file(path)
        elif "json" in path:
            product_report = read_json_file(path)

        if type == "simples":
            return SimpleReport.generate(product_report)
        elif type == "completo":
            return CompleteReport.generate(product_report)


Inventory.import_data("inventory_report/data/inventory.csv", 'simples')
