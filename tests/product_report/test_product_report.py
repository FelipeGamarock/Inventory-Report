from inventory_report.inventory.product import Product


def test_relatorio_produto():
    produto = Product(
        1,
        "bola",
        "Golaço",
        "18/10/2022",
        "18/10/2024",
        "123456",
        "não tem",
    )
    assert (
        str(produto)
        == "O produto bola fabricado em 18/10/2022 por Golaço "
        + "com validade até 18/10/2024 precisa ser armazenado não tem."
    )
