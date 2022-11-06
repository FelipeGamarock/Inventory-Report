import csv
import json
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


class Inventory:

    @classmethod
    def import_data(cls, path, type):
        if "csv" in path:
            if type == 'simples':
                with open(path, encoding="utf-8") as file:
                    product_reader = csv.DictReader(file)
                    print(product_reader)
                    product_list = [product for product in product_reader]
                    print(product_list)
                    return SimpleReport.generate(product_list)
            elif type == 'completo':
                with open(path, encoding="utf-8") as file:
                    product_reader = csv.DictReader(file)
                    print(product_reader)
                    product_list = [product for product in product_reader]
                    print(product_list)
                    return CompleteReport.generate(product_list)

        elif "json" in path:
            if type == 'simples':
                with open(path) as file:
                    product_list = json.load(file)
                    print(product_list)
                    return SimpleReport.generate(product_list)
            elif type == 'completo':
                with open(path) as file:
                    product_list = json.load(file)
                    print(product_list)
                    return CompleteReport.generate(product_list)


Inventory.import_data("inventory_report/data/inventory.csv", 'simples')
