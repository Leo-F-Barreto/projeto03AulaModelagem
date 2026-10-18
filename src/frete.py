def calcular_total(subtotal: float, regiao: str = "Norte") -> float:
    """
    Calcula o valor total do carrinho somando a taxa de frete com base no subtotal e na região de entrega.
    """
    # [RB-04] Valor inválido
    if subtotal <= 0:
        raise ValueError("Valor de carrinho inválido")

    regiao_formatada = regiao.strip().lower() if regiao else ""
    is_norte_nordeste = regiao_formatada in ["norte", "nordeste"]

    # [RB-03] Frete grátis para outras regiões (>= 250)
    if not is_norte_nordeste and subtotal >= 250.00:
        frete = 0.00

    # [RB-05] Frete grátis para Norte/Nordeste (> 300)
    elif is_norte_nordeste and subtotal > 300.00:
        frete = 0.00

    else:
        # [RB-01] Taxa de frete padrão
        frete = 15.00

        # [RB-02] Taxa adicional para regiões Norte e Nordeste
        if is_norte_nordeste:
            frete += 10.00

    return subtotal + frete
