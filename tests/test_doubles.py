import pytest
from unittest.mock import MagicMock

# CODIGO DE TESTE (pytest)
def test_finalizar_venda_com_sucesso():
    # 1. ARRANGE
    stub_ServicoLogisticaAPI = Mock()
    stub_ServicoLogisticaAPI.taxa_local.return_value = 25
    mock_enviar_notificacao_rastreio = Mock()
    dummy_user = Mock()

    # 2. ACT
    resultado = finalizar_venda(stub_ServicoLogisticaAPI, mock_enviar_notificacao_rastreio, dummy_user, frete_id=101)

    # 3. ASSERT
    assert resultado == "Sucesso"
    mock_email.enviar.assert_called_with(101)


def consulta_taxas_locais(stub_ServicoLogisticaAPI, mock_enviar_notificacao_rastreio, dummy_user, frete_id):
    print(f"\n[SUT] Processando frete {frete_id}...")

    # O Dummy é apenas passado, nunca usado.
    if dummy_user is not None:
        print("[SUT] Usuário identificado (Dummy apenas preenche o parâmetro).")

    # Stub fornece a resposta programada
    if stub_ServicoLogisticaAPI.taxa_local(25):
        print("[SUT] Taxa local identificada! (Resposta do Stub)")

        # Mock registra a ação
        mock_enviar_notificacao_rastreio.enviar(frete_id)
        print("[SUT] Comando de envio de e-mail disparado. (Ação para o Mock)")
        return "Sucesso"

    return "Falha"
