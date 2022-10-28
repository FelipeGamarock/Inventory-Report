from inventory_report.inventory.product import Product


def test_cria_produto():
    produto = Product(
        1,
        "bola",
        "Golaço",
        "18/10/2022",
        "18/10/2024",
        123456,
        "não tem",
    )
    assert produto.id == 1
    assert produto.nome_do_produto == "bola"
    assert produto.nome_da_empresa == "Golaço"
    assert produto.data_de_fabricacao == "18/10/2022"
    assert produto.data_de_validade == "18/10/2024"
    assert produto.numero_de_serie == 123456
    assert produto.instrucoes_de_armazenamento == "não tem"
