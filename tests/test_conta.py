import pytest
from src.conta import ContaBancaria

# ====================================================================
# TESTES DE REGRESSÃO (Funcionalidades Core Existentes)
# Garantem que as funções antigas não quebram com as novas adições
# ====================================================================

def test_deposito_sucesso():
    conta = ContaBancaria(100.0)
    conta.depositar(50.0)
    assert conta.saldo_corrente == 150.0

def test_deposito_invalido():
    conta = ContaBancaria()
    with pytest.raises(ValueError, match="Valor de depósito inválido"):
        conta.depositar(0)

def test_saque_sucesso():
    conta = ContaBancaria(100.0)
    conta.sacar(40.0)
    assert conta.saldo_corrente == 60.0

def test_saque_saldo_insuficiente():
    conta = ContaBancaria(50.0)
    with pytest.raises(ValueError, match="Saldo insuficiente na conta corrente"):
        conta.sacar(100.0)

# ====================================================================
# TESTES DA NOVA FUNCIONALIDADE (Investimento em Poupança)
# ====================================================================

def test_investir_poupanca_sucesso():
    conta = ContaBancaria(200.0)
    conta.investir_poupanca(50.0)
    
    # Verifica se descontou da corrente e foi pra poupança
    assert conta.saldo_corrente == 150.0
    assert conta.saldo_poupanca == 50.0

def test_investir_poupanca_saldo_insuficiente():
    conta = ContaBancaria(50.0)
    with pytest.raises(ValueError, match="Saldo insuficiente na conta corrente para investir"):
        conta.investir_poupanca(100.0)

def test_resgatar_poupanca_sucesso():
    conta = ContaBancaria(100.0)
    conta.investir_poupanca(100.0) # Move tudo pra poupança (Corrente: 0, Poupança: 100)
    
    conta.resgatar_poupanca(40.0) # Resgata 40
    assert conta.saldo_corrente == 40.0
    assert conta.saldo_poupanca == 60.0

def test_resgatar_poupanca_insuficiente():
    conta = ContaBancaria(100.0)
    conta.investir_poupanca(50.0)
    
    with pytest.raises(ValueError, match="Saldo insuficiente na poupança"):
        conta.resgatar_poupanca(60.0)
