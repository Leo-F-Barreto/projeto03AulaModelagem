from src.frete import calcular_total


def test_calculo_frete_Norte():
    # 1. ARRANGE
    # [RB-02] WHEN a região de entrega for "Norte" ou "Nordeste", THE SYSTEM SHALL adicionar uma taxa adicional de R$ 10,00 sobre a taxa base de frete.
    subtotal = 100.00
    regiao = "Norte"

    # 2. ACT
    resultado = calcular_total(subtotal, regiao)

    # 3. ASSERT
    assert resultado == 125.00


def test_calculo_frete_gratis_Norte():
    # 1. ARRANGE
    # [RB-03] IF o subtotal do carrinho for maior ou igual a R$ 300,00, THEN THE SYSTEM SHALL conceder frete grátis (taxa = R$ 0,00).
    subtotal = 450.00
    regiao = "Norte"

    # 2. ACT
    resultado = calcular_total(subtotal, regiao)

    # 3. ASSERT
    assert resultado == 450.00