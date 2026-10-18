from src.frete import calcular_total

def test_calculo_frete_padrao():
    """
    Testa se o valor total é calculado adicionando a taxa de frete padrão
    para subtotais abaixo de R$ 250,00.
    """
    # 1. ARRANGE
    # [RB-01] THE SYSTEM SHALL calcular o valor total adicionando a taxa de frete padrão de R$ 15,00 ao subtotal do carrinho.
    subtotal = 100.00

    # 2. ACT
    resultado = calcular_total(subtotal)

    # 3. ASSERT
    assert resultado == 115.00


def test_calculo_frete_gratis_limite_exato():
    """
    Testa se o frete é zerado quando o subtotal atinge exatamente R$ 250,00.
    """
    # 1. ARRANGE
    # [RB-02] IF o subtotal do carrinho for maior ou igual a R$ 250,00, THEN THE SYSTEM SHALL conceder frete grátis (taxa = R$ 0,00).
    subtotal = 250.00


    # 2. ACT
    resultado = calcular_total(subtotal)

    # 3. ASSERT
    assert resultado == 250.00
