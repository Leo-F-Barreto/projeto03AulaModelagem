from src.frete import calcular_total


def test_calculo_frete_Norte():
    # 1. ARRANGE
    subtotal = 275.00
    regiao = "Norte"

    # 2. ACT
    resultado = calcular_total(subtotal, regiao)

    # 3. ASSERT
    assert resultado == 300.00


def test_calculo_frete_gratis_Norte():
    # 1. ARRANGE
    subtotal = 450.00
    regiao = "Norte"

    # 2. ACT
    resultado = calcular_total(subtotal, regiao)

    # 3. ASSERT
    assert resultado == 450.00