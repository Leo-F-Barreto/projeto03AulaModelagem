def calcular_total(subtotal: float) -> float:
    """
    Calcula o valor total do carrinho somando a taxa de frete com base no subtotal.

    Regras de Negócio:
    - [RB-01]: Subtotal < R$ 250,00 adiciona taxa padrão de R$ 15,00.
    - [RB-02]: Subtotal >= R$ 250,00 concede frete grátis (taxa = R$ 0,00).
    """
    # [RB-02] IF o subtotal do carrinho for maior ou igual a R$ 250,00, THEN frete grátis
    if subtotal >= 250.00:
        frete = 0.00
    else:
        # [RB-01] Caso contrário, adiciona a taxa de frete padrão de R$ 15,00
        frete = 15.00

    return subtotal + frete
