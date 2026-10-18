def calcular_total(subtotal: float, regiao: str = "Norte") -> float:
    """
    Calcula o valor total do carrinho somando a taxa de frete com base no subtotal e na região de entrega.

    Regras de Negócio:
    - [RB-01]: Adiciona a taxa de frete padrão de R$ 15,00 ao subtotal do carrinho.
    - [RB-02]: Quando a região de entrega for "Norte" ou "Nordeste", adiciona taxa adicional de R$ 10,00 sobre a taxa base.
    - [RB-03]: Se o subtotal do carrinho for maior ou igual a R$ 300,00, concede frete grátis (taxa = R$ 0,00).
    - [RB-04]: Se subtotal <= 0, lança erro 'Valor de carrinho inválido'.
    """
    if subtotal <= 0:
        raise ValueError("Valor de carrinho inválido")

    # [RB-03] Frete grátis para compras a partir de R$ 300,00
    if subtotal >= 300.00:
        frete = 0.00
    else:
        # [RB-01] Taxa de frete padrão
        frete = 15.00

        # [RB-02] Taxa adicional para regiões Norte e Nordeste
        if regiao and regiao.strip().lower() in ["norte", "nordeste"]:
            frete += 10.00

    return subtotal + frete
